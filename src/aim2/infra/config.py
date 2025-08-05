from __future__ import annotations

from pathlib import Path
from typing import Dict, Type, TypeVar, ClassVar
import os
import yaml
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class AppSettings(BaseModel):
    """Application settings."""

    ENV_PREFIX: ClassVar[str] = "APP_"
    app_name: str
    debug: bool = False


def _read_yaml(path: Path) -> Dict[str, object]:
    with path.open("r") as handle:
        data = yaml.safe_load(handle)
    if data is None:
        data = {}
    return data


def _load_env_file(env_path: Path) -> None:
    if env_path.exists():
        with env_path.open("r") as handle:
            for line in handle:
                text = line.strip()
                if text and not text.startswith("#") and "=" in text:
                    key, value = text.split("=", 1)
                    if key not in os.environ:
                        os.environ[key] = value


def _apply_env(data: Dict[str, object], model: Type[T]) -> Dict[str, object]:
    prefix = ""
    if hasattr(model, "ENV_PREFIX"):
        prefix = getattr(model, "ENV_PREFIX")
    for field in model.model_fields:
        env_name = prefix + field.upper()
        if env_name in os.environ:
            data[field] = os.environ[env_name]
    return data


def load_config(path: Path, model: Type[T]) -> T:
    """Load configuration from a YAML file with environment overrides."""
    _load_env_file(path.parent / ".env")
    data = _read_yaml(path)
    data = _apply_env(data, model)
    return model(**data)
