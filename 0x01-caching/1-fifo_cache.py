#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFOCache class that inherits from BaseCaching
       and implements a FIFO caching system.
    '''

    def __init__(self):
        '''Initialize the class.'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''Add an item in the cache.'''
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discard = self.order.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

    def get(self, key):
        '''Get an item by key.'''
        return self.cache_data.get(key, None)
