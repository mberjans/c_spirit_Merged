from pathlib import Path

from aim2.ontology.schema import export_schema, load_schema


def test_roundtrip(tmp_path):
    source = Path("tests/fixtures/ontology/minimal_schema.yaml")
    schema = load_schema(source)
    out = tmp_path / "out.yaml"
    export_schema(schema, out)
    loaded = load_schema(out)
    assert "Item" in loaded.classes
