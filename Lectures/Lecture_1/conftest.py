import pytest
import yaml
from typing import Any

with open('config.yaml', encoding='utf-8') as f:
    data: Any = yaml.safe_load(f)


@pytest.fixture()
def coord1() -> tuple[Any, Any]:
    return data['lat'], data['long']


@pytest.fixture()
def text() -> Any:
    return data['text']


@pytest.fixture()
def limit() -> Any:
    return data['limit']


@pytest.fixture()
def radius() -> Any:
    return data['radius']
