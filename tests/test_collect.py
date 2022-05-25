"""Unit tests for pattern match collection.
"""

import pytest

import raider as rd

from .data import COLLECT_EXAMPLES


@pytest.mark.parametrize("coll, patterns, matches", COLLECT_EXAMPLES)
def test_collect(coll, patterns, matches):
    assert rd.collect(coll, patterns) == matches
