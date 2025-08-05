from importlib import import_module
from pathlib import Path
import random


def _has_test_target(text: str) -> bool:
    lines = text.splitlines()
    for line in lines:
        if line.strip().startswith("test:"):
            return True
    return False


def _mentions_pytest(text: str) -> bool:
    lines = text.splitlines()
    for line in lines:
        if "pytest" in line:
            return True
    return False


def test_makefile_has_pytest_target() -> None:
    makefile = Path("Makefile")
    assert makefile.exists()
    content = makefile.read_text()
    assert _has_test_target(content)
    assert _mentions_pytest(content)


def test_seed_sets_random_state() -> None:
    module = import_module("aim2.common.seed")
    module.set_seed(5)
    first = random.random()
    module.set_seed(5)
    second = random.random()
    assert first == second
