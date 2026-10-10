import pytest
from src.datasets.liverpool import load

@pytest.fixture
def frame():
    return load()
