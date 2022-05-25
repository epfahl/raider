"""Raider utility functions for both private and public use.
"""
from copy import deepcopy

from raider.exceptions import GeneralIndexError


def assoc(coll, key, value):
    """Return a new collection with an updated value for the given key.

    Examples
    --------
    >>> assoc({"a": 1}, "a", 2)
    {"a": 2}
    >>> assoc([1, 2], 0, 11)
    [11, 2]
    """
    coll_copy = deepcopy(coll)
    coll_copy[key] = value
    return coll_copy


def update_in(coll, path, func):
    """Return a new collection with an updated value at the given path, where
    the new value is the result of the application of the given function.  The
    collection can be nested dicts and lists.  An exception is raised if an
    index/key is not found.

    Examples
    --------
    >>> update_in({"a": 1}, ["a"], lambda x: x + 1)
    {"a": 2}
    >>> update_in([{"a": [1, 2]}], [0, "a", 1], lambda x: x * 2)
    [{"a": [1, 4]}]
    """

    def _inner(c, p, level):
        first, rest = p[0], p[1:]
        try:
            if not rest:
                return assoc(
                    c, first,
                    func(c[first]))
            else:
                return assoc(
                    c, first,
                    _inner(c[first], rest, level + 1))
        except (KeyError, IndexError):
            index = f"'{first}'" if isinstance(first, str) else first
            raise GeneralIndexError(
                f"The collection does not have index {index} at level {level}."
            )

    return _inner(coll, path, 0)


def assoc_in(coll, path, value):
    """Return a new collection with an updated value at the given path.  The
    collection can be nested dicts and lists.  An exception is raised if an
    index/key is not found.

    Examples
    --------
    >>> assoc_in({"a": 1}, ["a"], 2)
    {"a": 2}
    >>> assoc_in([{"a": [1, 2]}], [0, "a", 0], 11)
    [{"a": [11, 2]}]
    """
    return update_in(coll, path, lambda x: value)


def is_struct(dct, keys, match=False):
    """Return True if the given dict has the given keys.  If the match
    parameter is True, the set of given keys must equal the set of dict keys.
    When match is False, the set of given can be a subset of the dict keys.

    Examples
    --------
    >>> is_struct({"a": 1, "b": 2}, ["a", "b"])
    True
    >>> is_struct({"a": 1}, ["b"])
    False
    >>> is_struct(None, [])
    False
    >>> is_struct({}, [])
    """
    if not isinstance(keys, (list, set)):
        raise TypeError("The given keys must be a list or set.")
    if not isinstance(dct, dict) or not dct:
        return False
    dct_keys = set(dct.keys())
    query_keys = set(keys)
    if match:
        return dct_keys == query_keys
    else:
        return query_keys.issubset(dct_keys)
