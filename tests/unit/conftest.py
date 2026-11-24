"""Unit-tier conftest."""

from pathlib import Path

import pytest


@pytest.fixture
def canopus_patterns_resources_path():
    return Path("tests/resources/")
