"""Unit tests for pattern match updating.
"""

import pytest

import raider as rd

from .data import UPDATE_EXAMPLES


@pytest.mark.parametrize("coll, matches, matches_updated", UPDATE_EXAMPLES)
def test_collect(coll, matches, matches_updated):
    assert rd.update(coll, matches) == matches_updated
