"""Unit tests for tools functions.
"""

import pytest

from raider import tools
from raider.exceptions import GeneralIndexError

from .data import ASSOC_EXAMPLES, ASSOC_IN_EXAMPLES, UPDATE_IN_EXAMPLES


@pytest.mark.parametrize("coll, key, value, result", ASSOC_EXAMPLES)
def test_assoc(coll, key, value, result):
    assert tools.assoc(coll, key, value) == result
    assert coll != result


@pytest.mark.parametrize("coll, path, func, result", UPDATE_IN_EXAMPLES)
def test_update_in(coll, path, func, result):
    assert tools.update_in(coll, path, func) == result
    assert coll != result


@pytest.mark.parametrize("coll, path, value, result", ASSOC_IN_EXAMPLES)
def test_assoc_in(coll, path, value, result):
    assert tools.assoc_in(coll, path, value) == result
    assert coll != result


def test_update_in_fail():
    with pytest.raises(GeneralIndexError):
        tools.update_in({"a": 1}, ["b"], lambda x: x)


def test_is_struct():
    assert tools.is_struct({"a": 1, "b": 1}, ["a", "b"])
    assert tools.is_struct({"a": 1, "b": 1}, ["a"])
    assert not tools.is_struct({"a": 1, "b": 1}, ["a"], match=True)
    assert not tools.is_struct({}, [])


def test_is_struct_fail():
    with pytest.raises(TypeError):
        tools.is_struct({}, None)
