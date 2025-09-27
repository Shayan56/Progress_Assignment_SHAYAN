import pytest
from app import greet


def test_greet():
    assert greet("Shayan") == "Hello, Shayan!"  # nosec B101
