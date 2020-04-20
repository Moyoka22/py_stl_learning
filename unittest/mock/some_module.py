import json


def some_function(s: str) -> float:
    """Does some stuff, written without dependency injection which complicates testing somewhat"""
    _obj = json.loads(s)
    return getattr(_obj, 'ttl')
