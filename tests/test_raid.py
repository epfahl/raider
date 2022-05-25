"""Unit tests for collecting, updating, and inserting (i.e., raiding).
"""

import pytest

import raider as rd

from .data import RAID_EXAMPLES


@pytest.mark.parametrize(
    "coll, patterns, updates, coll_updated", RAID_EXAMPLES)
def test_insert(coll, patterns, updates, coll_updated):
    assert rd.raid(coll, patterns, updates) == coll_updated
