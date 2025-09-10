class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]   # each index has a bucket (list)

    def _hash(self, key):
        """Better hash function using Python's built-in hash()"""
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:  # key exists → update
                bucket[i] = (key, value)
                return
        bucket.append((key, value))  # otherwise, insert new

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # not found

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Index {i}: {bucket}")


ht = HashTable(10)
ht.set("name", "Alice")
ht.set("age", 25)
ht.set("city", "Paris")

print(ht.get("name"))   
print(ht.get("city")) 

ht.remove("age")
ht.display()
