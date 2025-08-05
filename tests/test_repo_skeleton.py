from importlib import import_module
import pytest


def test_import_aim2():
    module = import_module("aim2")
    assert module is not None


def test_version_attribute():
    module = import_module("aim2")
    version = getattr(module, "__version__")
    parts = version.split(".")
    assert len(parts) == 3


def test_missing_module_error():
    with pytest.raises(ModuleNotFoundError):
        import_module("aim2.nonexistent")
