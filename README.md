# Raider

Descend into the dark depths of uncharted data structures.  Discover relics deserving of display.  Diligently displace those relics with... sand?  Well, hopefully something better than sand.

<p align="center">
  <img width="550" src="indy.jpg">
</p>

## Installation

Clone the repo and start using it. `Raider` is a pure Python library with no external dependencies.

## Usage

For most scenarios, the most sensible course will be to use the `raid` function as follows:

```
import raider
updated_collection = raider.raid(collection, patterns, updates)
```

where `collection` is a nested data structure comprised of dictionaries and lists, `patterns` is a list of named boolean functions that signal a value pattern match, and `updates` specifies named transformation functions to be applied to pattern-matched values.  

Here is a full set of example arguments:

```
collection = {"a": 1, "b": [{"c": 2, "d": 3}]}

patterns = [
    {
        "name": "one",
        "func": lambda v: isinstance(v, int) and v > 1
    }
]

updates = [
    {
        "name": "one",
        "func": lambda v: v * 100
    }
]
```

Application of `raider.raid` yields the updated collection:

```
{'a': 1, 'b': [{'c': 200, 'd': 300}]}
```
