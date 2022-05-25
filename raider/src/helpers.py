"""Private helpers functions.
"""

from raider import tools as rt
from raider.exceptions import InvalidObjectsError


def _validate_object(pos, obj, obj_name, keys):
    if not rt.is_struct(obj, keys):
        raise InvalidObjectsError(
            f"{obj_name.capitalize()} {pos} must be a dict with keys {keys}."
        )
    return obj


def validate_objects(objs, obj_name, keys):
    """Validate the rule set (either collection patterns or update rules) and
    return the rules if no errors are found.
    """

    def _validate(pos, obj):
        return _validate_object(pos, obj, obj_name, keys)

    if not isinstance(objs, list):
        raise InvalidObjectsError(
            f"Input {obj_name} must be a list of {obj_name} objects, not an "
            f"object of type '{type(objs).__name__}'."
        )
    return [_validate(i, o) for i, o in enumerate(objs)]
