from collections import OrderedDict

CACHE_SIZE = 10
cache = OrderedDict()

def get_cache(key):
    return cache.get(key)

def add_to_cache(key, value):
    if key in cache:
        cache.pop(key)

    cache[key] = value

    if len(cache) > CACHE_SIZE:
        cache.popitem(last=False)

def clear_cache():
    cache.clear()
