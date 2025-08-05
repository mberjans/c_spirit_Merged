"""Utilities for deterministic behavior."""

from __future__ import annotations

import os
import random


def set_seed(value: int) -> None:
    random.seed(value)
    os.environ["PYTHONHASHSEED"] = str(value)
