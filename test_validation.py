#!/usr/bin/env python3
import json
import jsonschema
from jsonschema import validate

def test_invalid_month():
    # Test with invalid month format
    invalid_json = {
        "themes": [
            {
                "name": "Test Theme",
                "items": [
                    {
                        "line": {
                            "items": [
                                {
                                    "type": "bar",
                                    "label": "Test Bar",
                                    "start": "Jan",
                                    "end": "InvalidMonth",  # This should fail validation
                                    "year": 2026
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }

    # Load the schema
    with open("data/roadmap_schema.json", "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=invalid_json, schema=schema)
        print("❌ This should not have passed validation!")
    except jsonschema.exceptions.ValidationError as e:
        print(f"✅ Validation correctly caught the error: {e.message}")
        print(f"   Invalid value: '{e.instance}' is not one of {e.schema['enum']}")

if __name__ == "__main__":
    test_invalid_month()
