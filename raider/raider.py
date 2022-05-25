"""Public Raider API.
"""

from raider.src import collecting, updating, inserting


def collect(coll, patterns):
    """
    """
    return collecting.collect(coll, patterns)


def update(matches, updates):
    """
    """
    return updating.update(matches, updates)


def insert(matches, coll):
    """
    """
    return inserting.insert(matches, coll)


def raid(coll, patterns, updates):
    """
    """
    return insert(update(collect(coll, patterns), updates), coll)
