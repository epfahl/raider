"""Unit tests for private helper functions.
"""

import pytest

from raider.src import helpers as rh
from raider.exceptions import InvalidObjectsError


def test_validate_objects():
    objs = [{"name": None, "func": None}]
    assert rh.validate_objects(objs, "", ["name", "func"]) == objs


def test_validate_objects_list_fail():
    with pytest.raises(InvalidObjectsError):
        rh.validate_objects(lambda x: x, "", ["name", "func"])


def test_validate_objects_struct_fail():
    with pytest.raises(InvalidObjectsError):
        rh.validate_objects(
            [{"name": None, "rule": None}], "", ["name", "func"])
