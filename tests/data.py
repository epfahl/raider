"""Static data for unit tests.
"""

from raider import tools

# (collection, patterns, matches)
COLLECT_EXAMPLES = [
    (
        {"a": 1, "b": 2},
        [
            {"name": "one", "func": lambda v: v == 1}
        ],
        [
            {"path": ["a"], "pattern": "one", "value": 1}
        ]
    ),
    (
        {"a": 1, "b": [1, 2, 3]},
        [
            {"name": "one", "func": lambda v: v == 1},
            {"name": "two", "func": lambda v: v == 2}
        ],
        [
            {"path": ["a"], "pattern": "one", "value": 1},
            {"path": ["b", 0], "pattern": "one", "value": 1},
            {"path": ["b", 1], "pattern": "two", "value": 2}
        ]
    ),
    (
        {"a": 1, "b": [{"c": 2, "d": 3}]},
        [
            {
                "name": "has_cd",
                "func": lambda v: tools.is_struct(v, ["c", "d"])
            }
        ],
        [
            {"path": ["b", 0], "pattern": "has_cd", "value": {"c": 2, "d": 3}}
        ]
    ),
    (
        [1, "a", 3],
        [
            {"name": "a", "func": lambda v: v == "a"}
        ],
        [
            {"path": [1], "pattern": "a", "value": "a"}
        ]
    ),
    (
        [1, ["a", "b"], 3],
        [
            {"name": "in_ab", "func": lambda v: v in ("a", "b")}
        ],
        [
            {"path": [1, 0], "pattern": "in_ab", "value": "a"},
            {"path": [1, 1], "pattern": "in_ab", "value": "b"}
        ]
    ),
    (
        [1, [{"a": 1, "b": 2}], 3],
        [
            {"name": "two", "func": lambda v: v == 2}
        ],
        [
            {"path": [1, 0, "b"], "pattern": "two", "value": 2}
        ]
    )
]

# (matches, updates, updated matches)
UPDATE_EXAMPLES = [
    (
        [
            {"path": ["a"], "pattern": "one", "value": 1},
            {"path": ["b", 0], "pattern": "one", "value": 1},
            {"path": ["b", 1], "pattern": "two", "value": 2}
        ],
        [
            {"name": "two", "func": lambda v: v * 10}
        ],
        [
            {"path": ["a"], "pattern": "one", "value": 1},
            {"path": ["b", 0], "pattern": "one", "value": 1},
            {"path": ["b", 1], "pattern": "two", "value": 20}
        ]
    )
]

# (matches, collection, updated collection)
INSERT_EXAMPLES = [
    (
        [
            {'path': ['b', 0, 'c'], 'pattern': 'one', 'value': 20},
            {'path': ['b', 0, 'd'], 'pattern': 'one', 'value': 30}
        ],
        {"a": 1, "b": [{"c": 2, "d": 3}]},
        {"a": 1, "b": [{"c": 20, "d": 30}]}
    )
]

# (coll, patterns, updates, updated collection)
RAID_EXAMPLES = [
    (
        {"a": 1, "b": [{"c": 2, "d": 3}]},
        [
            {
                "name": "one",
                "func": lambda v: isinstance(v, int) and v > 1
            }
        ],
        [
            {
                "name": "one",
                "func": lambda v: v * 10
            }
        ],
        {"a": 1, "b": [{"c": 20, "d": 30}]}
    )
]

ASSOC_EXAMPLES = [
    ({"a": 1}, "a", 2, {"a": 2}),
    ([1, 2], 0, 11, [11, 2])
]

ASSOC_IN_EXAMPLES = [
    ({"a": 1}, ["a"], 2, {"a": 2}),
    ([{"a": [1, 2]}], [0, "a", 0], 11, [{"a": [11, 2]}])
]

UPDATE_IN_EXAMPLES = [
    ({"a": 1}, ["a"], lambda x: x + 1, {"a": 2}),
    ([{"a": [1, 2]}], [0, "a", 1], lambda x: x * 2, [{"a": [1, 4]}])
]
