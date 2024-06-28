#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    '''LFUCache class that inherits from BaseCaching
       and implements an LFU caching system.
    '''

    def __init__(self):
        '''Initialize the class.'''
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        '''Add an item in the cache.'''
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self._update_usage_order(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self._evict_least_frequently_used()

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def get(self, key):
        '''Get an item by key.'''
        if key in self.cache_data:
            self.frequency[key] += 1
            self._update_usage_order(key)
            return self.cache_data[key]
        return None

    def _update_usage_order(self, key):
        '''Update the usage order of the key.'''
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def _evict_least_frequently_used(self):
        '''Evict the least frequently used item.'''
        if not self.usage_order:
            return

        min_freq = min(self.frequency.values())
        leastFrequent = [k for k, v in self.frequency.items() if v == min_freq]

        if len(leastFrequent) > 1:
            for key in self.usage_order:
                if key in leastFrequent:
                    self.usage_order.remove(key)
                    break
        else:
            key = leastFrequent[0]
            self.usage_order.remove(key)

        del self.cache_data[key]
        del self.frequency[key]
        print(f"DISCARD: {key}")
