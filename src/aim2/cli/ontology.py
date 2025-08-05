import argparse
from pathlib import Path

from aim2.ontology.schema import load_schema


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--schema", type=Path, required=True, help="Path to schema YAML"
    )
    args = parser.parse_args()
    schema = load_schema(args.schema)
    count = len(schema.classes)
    print(str(count))
