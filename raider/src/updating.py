"""Update match objects.
"""

from raider.src import helpers as rh


def _filter_matches(matches, update_patterns):
    """Return a list of only those match objects for which the pattern name is
    in the list of update pattern names.
    """
    return [match for match in matches if match["pattern"] in update_patterns]


def _update_names(updates):
    """Return a list of update pattern names.
    """
    return [upd[0] for upd in updates]


def _update_fn(pattern, updates):
    """Return the name of the first matching pattern, or return None if no
    pattern matches.
    """
    return next(
        (u["func"] for u in updates if u["name"] == pattern),
        lambda x: x)


def update(matches, updates):
    """Given a list of value match objects and update rules, return a list of
    match objects with updated values.
    """

    updates = rh.validate_objects(updates, "update", ["name", "func"])

    def _update(match):
        value, path, pattern = match["value"], match["path"], match["pattern"]
        value_update = _update_fn(pattern, updates)(value)
        return {
            "path": path,
            "value": value_update,
            "pattern": pattern
        }

    return list(map(_update, matches))
