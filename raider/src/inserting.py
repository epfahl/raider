"""Insert updated values in match objects into a collection.
"""

from functools import reduce

from raider import tools as rt
from raider.src import helpers as rh


def insert(matches, coll):
    """Insert each match value into the collection according to each match
    path.
    """

    matches = rh.validate_objects(
        matches, "match", ["path", "value", "pattern"])

    def _insert(m):
        """Insert a single match.
        """
        return lambda c: rt.assoc_in(c, m["path"], m["value"])

    return reduce(
        lambda c, fn: fn(c),
        map(_insert, matches),
        coll)
