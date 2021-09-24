from pipeline.locator import get
from datetime import datetime
import pytest


def test_get_returns_requested_function():
    assert get("datetime.datetime") == datetime


def test_get_raises_if_requested_is_not_callable():
    with pytest.raises(ImportError):
        assert get("datetime.datetime.year")

