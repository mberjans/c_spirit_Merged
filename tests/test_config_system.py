from importlib import import_module
from pathlib import Path
import os
import pytest


def _write_yaml(path, content):
    lines = content.split("\n")
    with path.open("w") as handle:
        for line in lines:
            handle.write(line + "\n")


def test_loads_yaml_file(tmp_path: Path) -> None:
    config_path = tmp_path / "app.yaml"
    _write_yaml(config_path, "app_name: demo\ndebug: true")
    config_module = import_module("aim2.infra.config")
    load_config = getattr(config_module, "load_config")
    settings_class = getattr(config_module, "AppSettings")
    settings = load_config(config_path, settings_class)
    assert settings.app_name == "demo"
    assert settings.debug is True


def test_environment_overrides_yaml(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config_path = tmp_path / "app.yaml"
    _write_yaml(config_path, "app_name: demo\ndebug: false")
    monkeypatch.setenv("APP_APP_NAME", "override")
    config_module = import_module("aim2.infra.config")
    load_config = getattr(config_module, "load_config")
    settings_class = getattr(config_module, "AppSettings")
    settings = load_config(config_path, settings_class)
    assert settings.app_name == "override"


def test_missing_required_field_raises(tmp_path: Path) -> None:
    config_path = tmp_path / "app.yaml"
    _write_yaml(config_path, "debug: true")
    config_module = import_module("aim2.infra.config")
    load_config = getattr(config_module, "load_config")
    settings_class = getattr(config_module, "AppSettings")
    with pytest.raises(Exception):
        load_config(config_path, settings_class)
