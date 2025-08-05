from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml


@dataclass
class ClassDef:
    """Definition for a single class in the ontology schema."""

    label: str
    synonyms: List[str]
    definition: str
    xrefs: List[str]


@dataclass
class OntologySchema:
    """Container for classes and slots in the ontology schema."""

    classes: Dict[str, ClassDef]
    slots: Dict[str, Any]


def _ensure_string_list(value, field, name):
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValueError(field + " must be a list for " + name)
    result: List[str] = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError(field + " entries must be strings for " + name)
        result.append(item)
    return result


def load_schema(path: Path) -> OntologySchema:
    """Load a YAML schema file into an :class:`OntologySchema`.

    Parameters
    ----------
    path:
        Location of the YAML schema file.

    Returns
    -------
    OntologySchema
        Parsed schema object with classes and slots.

    Raises
    ------
    ValueError
        If required fields are missing or invalid in the schema.
    """

    text = path.read_text()
    data = yaml.safe_load(text)
    if "classes" not in data:
        raise ValueError("classes section is required")
    classes: Dict[str, ClassDef] = {}
    for name, attrs in data["classes"].items():
        label = attrs.get("label")
        if label is None:
            raise ValueError("label is required for " + name)
        synonyms = _ensure_string_list(attrs.get("synonyms"), "synonyms", name)
        definition = attrs.get("definition")
        if definition is None:
            raise ValueError("definition is required for " + name)
        xrefs = _ensure_string_list(attrs.get("xrefs"), "xrefs", name)
        class_def = ClassDef(
            label=label, synonyms=synonyms, definition=definition, xrefs=xrefs
        )
        classes[name] = class_def
    slots = data.get("slots") or {}
    schema = OntologySchema(classes=classes, slots=slots)
    return schema


def export_schema(schema: OntologySchema, path: Path) -> None:
    data: Dict[str, Any] = {"classes": {}, "slots": schema.slots}
    for name, class_def in schema.classes.items():
        entry: Dict[str, Any] = {}
        entry["label"] = class_def.label
        entry["synonyms"] = class_def.synonyms
        entry["definition"] = class_def.definition
        entry["xrefs"] = class_def.xrefs
        data["classes"][name] = entry
    text = yaml.safe_dump(data)
    path.write_text(text)
