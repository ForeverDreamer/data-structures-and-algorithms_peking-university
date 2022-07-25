class HashTable:
    def __init__(self):
        self._size = 11
        self._keys = [None] * self._size
        self._values = [None] * self._size

    @property
    def keys(self):
        return self._keys

    @property
    def values(self):
        return self._values

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
                # 找到key, key已存在，更新value
                if self._keys[next_hashvalue]:
                    self._values[next_hashvalue] = value
                # 找到空位，key不存在，同时保存key和value
                else:
                    self._keys[next_hashvalue] = key
                    self._values[next_hashvalue] = value

    def get(self, key):
        start_hash = self.hashfunction(key)
        value = None
        current_hash = start_hash

        while self._keys[current_hash]:
            if self._keys[current_hash] == key:
                value = self._values[current_hash]
                break
            else:
                current_hash = self.rehash(current_hash)
                if current_hash == start_hash:
                    break
        return value


if __name__ == '__main__':
    h = HashTable()
    h[54] = 'cat'
    h[26] = 'dog'
    h[93] = 'lion'
    h[17] = 'tiger'
    h[77] = 'bird'
    h[31] = 'cow'
    h[44] = 'goat'
    h[55] = 'pig'
    h[20] = 'chicken'
    print(h.keys)
    print(h.values)
    print(h[20])
    print(h[17])
    h[20] = 'duck'
    print(h[20])
    print(h[99])
