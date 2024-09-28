# MEMO: Redisなどに置き換える

cache = {}

class Cache:
    def __init__(self, prefix='cache:'):
        self.cache = {}
        self.prefix = prefix

    def get(self, key):
        return cache.get(self.prefix + key)

    def set(self, key, value):
        cache[self.prefix + key] = value

    def delete(self, key):
        del cache[self.prefix + key]

    def all(self):
        return cache

    def clear(self):
        cache.clear()
