import subprocess
from pathlib import Path


def test_cli_loads_schema():
    schema_path = Path("tests/fixtures/ontology/minimal_schema.yaml")
    result = subprocess.run(
        [
            "aim2-ontology",
            "--schema",
            str(schema_path),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "1" in result.stdout
