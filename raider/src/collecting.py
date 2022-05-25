"""Collect pattern-matched values and their paths in a nested data structure.
"""

from raider.src import helpers as rh


def _pack_match(value, path, pattern_name):
    """Return a dict containing the value, path, and pattern name of the match.
    """
    return {
        "value": value,
        "path": path,
        "pattern": pattern_name
    }


def _is_collection(x):
    """Return True if the input is a list or dict.
    """
    return isinstance(x, (list, dict))


def _list_keyvals(coll):
    """Return a list of key-value pairs for the given collection.  If the
    collection is a list, the result is a list of index-value pairs.
    """
    if isinstance(coll, list):
        return list(enumerate(coll))
    elif isinstance(coll, dict):
        return list(coll.items())
    raise ValueError(
        f"Input must be a list or dict, not type {type(coll).__name__}"
    )


def _find_match(value, patterns):
    """Return the name of the first matching pattern, or return None if no
    pattern matches.
    """
    return next((p["name"] for p in patterns if p["func"](value)), None)


def _collect_on_patterns(patterns):
    """Return a function that recursively accumulates a list of values and
    corresponding paths for which for which on or named patterns are
    satisfied.
    """

    def _collector(keyvals, path):

        def _split(first, rest, path):
            return first + _collector(rest, path)

        if not keyvals:
            return []

        (key, value), rest = keyvals[0], keyvals[1:]
        path_update = path + [key]

        pattern_name = _find_match(value, patterns)

        if pattern_name is not None:
            return _split(
                [_pack_match(value, path_update, pattern_name)],
                rest, path)
        elif not _is_collection(value):
            return _split([], rest, path)
        else:
            return _split(
                _collector(_list_keyvals(value), path_update),
                rest, path)

    return _collector


def collect(coll, patterns):
    """For the given (possibly nested) collection, return a list of values and
    corresponding paths for which one or more named patterns are satisfied.
    """
    patterns = rh.validate_objects(patterns, "pattern", ["name", "func"])
    if not patterns:
        return coll
    collector = _collect_on_patterns(patterns)
    return collector(_list_keyvals(coll), [])
