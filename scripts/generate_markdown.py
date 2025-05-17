#!/usr/bin/env python3
import json
import os

def generate_markdown(index_path="site/blueprint_index.json", output_path="site/index.md"):
    with open(index_path, "r") as f:
        blueprints = json.load(f)

    lines = [
        "# 🧠 John Stetter’s Home Assistant Blueprints",
        "",
        "Automatically generated index of all published blueprints.",
        "",
        "| Name | Domain | Description | Import URL |",
        "|------|--------|-------------|------------|",
    ]

    for bp in blueprints:
        name = bp["name"]
        domain = bp["domain"]
        description = bp["description"]
        path = bp["path"]
        raw_url = f"https://raw.githubusercontent.com/johnstetter/home-assistant-blueprints/main/{path}"
        lines.append(f"| **{name}** | `{domain}` | {description} | [Import]({raw_url}) |")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    generate_markdown()
