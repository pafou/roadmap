#!/usr/bin/env python3
import json
import jsonschema
from jsonschema import validate

def validate_json_against_schema(json_file, schema_file):
    try:
        # Load the JSON data
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        # Load the schema
        with open(schema_file, 'r', encoding='utf-8') as f:
            schema = json.load(f)

        # Validate
        validate(instance=json_data, schema=schema)
        print("✅ JSON is valid against the schema!")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        return False
    except jsonschema.exceptions.ValidationError as e:
        print(f"❌ JSON validation error: {e.message}")
        print(f"   Path: {' -> '.join(str(x) for x in e.path)}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    # Validate the roadmap JSON against the schema
    validate_json_against_schema("data/roadmap.json", "data/roadmap_schema.json")
