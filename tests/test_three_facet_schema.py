import pytest

from aim2.ontology.schema import load_schema


def test_load_valid_schema(tmp_path):
    yaml_text = """classes:\n  Item:\n    label: Sample\n    synonyms:\n      - Example\n    definition: Sample item\n    xrefs:\n      - EX:1\nslots: {}\n"""
    schema_file = tmp_path / "schema.yaml"
    schema_file.write_text(yaml_text)
    schema = load_schema(schema_file)
    assert hasattr(schema, "classes")
    assert "Item" in schema.classes


def test_missing_label_raises(tmp_path):
    yaml_text = """classes:\n  Item:\n    synonyms:\n      - Example\n    definition: Sample item\n    xrefs:\n      - EX:1\n"""
    schema_file = tmp_path / "schema.yaml"
    schema_file.write_text(yaml_text)
    with pytest.raises(ValueError):
        load_schema(schema_file)


def test_synonyms_not_list_raises(tmp_path):
    yaml_text = """classes:\n  Item:\n    label: Sample\n    synonyms: Example\n    definition: Sample item\n    xrefs:\n      - EX:1\n"""
    schema_file = tmp_path / "schema.yaml"
    schema_file.write_text(yaml_text)
    with pytest.raises(ValueError):
        load_schema(schema_file)
