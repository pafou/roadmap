#!/usr/bin/env python3
"""
YAML Validator - Validates roadmap.yaml file
Usage: python3 yaml_validator.py
"""

import yaml
import sys
import time
import os

def validate_yaml(yaml_file="data/roadmap.yaml"):
    """
    Validate a YAML file and return True if valid, False otherwise
    """
    try:
        with open(yaml_file, 'r') as f:
            yaml_content = f.read()

        # Try to parse the YAML
        yaml.safe_load(yaml_content)
        return True, "✅ YAML is valid and well-formed"

    except yaml.YAMLError as e:
        return False, f"❌ YAML Error: {e}"
    except FileNotFoundError:
        return False, f"❌ File '{yaml_file}' not found"
    except Exception as e:
        return False, f"❌ Error reading file: {e}"

def main():
    yaml_file = "data/roadmap.yaml"

    print(f"🔍 Validating {yaml_file}...")
    is_valid, message = validate_yaml(yaml_file)
    print(message)

    # Show additional info if valid
    if is_valid:
        try:
            with open(yaml_file, 'r') as f:
                content = f.read()
            lines = content.split('\n')
            print(f"📊 File stats: {len(lines)} lines")

            # Count themes and items
            import yaml
            data = yaml.safe_load(content)
            theme_count = len(data.get('themes', []))
            item_count = sum(len(theme.get('items', [])) for theme in data.get('themes', []))
            print(f"📋 Structure: {theme_count} themes, {item_count} items")

        except Exception:
            pass  # Don't fail if we can't show extra info

    return 0 if is_valid else 1

def continuous_watch():
    """
    Watch the YAML file for changes and validate automatically
    """
    yaml_file = "data/roadmap.yaml"
    last_modified = os.path.getmtime(yaml_file)

    print(f"👀 Watching {yaml_file} for changes...")
    print("Press Ctrl+C to stop watching")

    try:
        while True:
            current_modified = os.path.getmtime(yaml_file)
            if current_modified > last_modified:
                print(f"\n📝 {yaml_file} changed - validating...")
                is_valid, message = validate_yaml(yaml_file)
                print(message)
                last_modified = current_modified
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopped watching")

if __name__ == "__main__":
    # Check if we should run in watch mode
    if len(sys.argv) > 1 and sys.argv[1] == "--watch":
        continuous_watch()
    else:
        # Normal validation mode
        sys.exit(main())
