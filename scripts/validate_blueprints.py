#!/usr/bin/env python3

import os
import yaml
import sys

def find_blueprints(path):
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                yield os.path.join(root, file)

def validate_blueprint_structure(file_path):
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(f"❌ YAML error in {file_path}: {exc}")
            return False

        blueprint = data.get('blueprint')
        if not blueprint:
            print(f"❌ Missing 'blueprint:' section in {file_path}")
            return False

        required_fields = ['name', 'description', 'domain', 'input']
        missing = [field for field in required_fields if field not in blueprint]
        if missing:
            print(f"❌ {file_path} is missing fields: {missing}")
            return False

    print(f"✅ {file_path} is a valid blueprint")
    return True

def main():
    base_path = "blueprints"
    failed = False

    for file_path in find_blueprints(base_path):
        if not validate_blueprint_structure(file_path):
            failed = True

    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
