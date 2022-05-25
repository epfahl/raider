"""Unit tests for pattern match instertion.
"""

import pytest

import raider as rd

from .data import INSERT_EXAMPLES


@pytest.mark.parametrize("matches, coll, coll_updated", INSERT_EXAMPLES)
def test_insert(matches, coll, coll_updated):
    assert rd.insert(matches, coll) == coll_updated
