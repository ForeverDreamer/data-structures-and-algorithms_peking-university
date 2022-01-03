class HashTable:
    def __init__(self):
        self._size = 11
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def hashfunction(self, key):
        return key % self._size

    def rehash(self, oldhash):
        return (oldhash + 1) % self._size

    def put(self, key, value):
        hashvalue = self.hashfunction(key)
        if self._keys[hashvalue] is None:
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
        else:
            if self._keys[hashvalue] == key:
                self._values[hashvalue] = value
            else:
                next_hashvalue = self.rehash(hashvalue)
                while self._keys[next_hashvalue] and self._keys[next_hashvalue] != key:
                    next_hashvalue = self.rehash(next_hashvalue)
                if self._keys[next_hashvalue]:
                    self._values[next_hashvalue] = value
                else:
                    self._keys[next_hashvalue] = key
                    self._values[next_hashvalue] = value

    def get(self, key):
        start = self.hashfunction(key)
        value = None
        stop = False
        found = False
        current = start

        while self._keys[current] and (not found) and (not stop):
            if self._keys[current] == key:
                found = True
                value = self._values[current]
            else:
                current = self.rehash(current)
                if current == start:
                    stop = True
        return value
