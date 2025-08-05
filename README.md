# AIM2

Toolkit for ontology development and information extraction.

## Example
```python
from aim2 import get_version
print(get_version())
```

## Reproducible environment
```bash
make test
```
```python
from aim2.common.seed import set_seed
set_seed(0)
```

## Configuration system
```python
from pathlib import Path
from aim2.infra.config import AppSettings, load_config

settings = load_config(Path("app.yaml"), AppSettings)
print(settings.app_name)
```
