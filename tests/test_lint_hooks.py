from pathlib import Path


def _has_text(lines: list[str], expected: str) -> bool:
    """Return True if expected text appears in lines."""
    for line in lines:
        if expected in line:
            return True
    return False


def test_pre_commit_has_lint_hooks():
    path = Path(".pre-commit-config.yaml")
    assert path.exists()
    content = path.read_text().splitlines()
    assert _has_text(content, "ruff"), "ruff hook missing"
    assert _has_text(content, "isort"), "isort hook missing"
    assert _has_text(content, "black"), "black hook missing"


def test_pyproject_has_tool_sections():
    path = Path("pyproject.toml")
    assert path.exists()
    content = path.read_text().splitlines()
    assert _has_text(content, "[tool.ruff]"), "ruff config missing"
    assert _has_text(content, "[tool.isort]"), "isort config missing"
