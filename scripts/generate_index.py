import os
import yaml
import json

def find_blueprints(base_dir):
    index = []

    class BlueprintLoader(yaml.SafeLoader):
        pass

    def ignore_unknown_tags(loader, tag_suffix, node):
        return loader.construct_scalar(node)

    BlueprintLoader.add_multi_constructor("!", ignore_unknown_tags)

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".yaml"):
                full_path = os.path.join(root, file)
                with open(full_path, "r") as f:
                    try:
                        data = yaml.load(f, Loader=BlueprintLoader)
                        bp = data.get("blueprint", {})
                        if bp:
                            index.append({
                                "name": bp.get("name"),
                                "description": bp.get("description"),
                                "domain": bp.get("domain"),
                                "path": full_path.replace("\\", "/")
                            })
                    except Exception as e:
                        print(f"Error parsing {full_path}: {e}")
    return index

if __name__ == "__main__":
    index = find_blueprints("blueprints")
    os.makedirs("site", exist_ok=True)
    with open("site/blueprint_index.json", "w") as f:
        json.dump(index, f, indent=2)
