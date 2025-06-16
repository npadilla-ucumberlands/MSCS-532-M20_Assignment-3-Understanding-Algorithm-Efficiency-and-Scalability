import time

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        self.table[index].append((key, value))  # Insert new key-value pair

    def search(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, (k, _) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False

    def __str__(self):
        return str(self.table)


# --- Sample Functional Tests ---
if __name__ == "__main__":
    print("Basic functionality test:\n")

    ht = HashTable(size=5)
    ht.insert("apple", 100)
    ht.insert("banana", 200)
    ht.insert("grape", 300)
    ht.insert("banana", 250)  # Update
    ht.insert("lemon", 150)

    print("Search 'banana':", ht.search("banana"))
    print("Delete 'apple':", ht.delete("apple"))
    print("Search 'apple':", ht.search("apple"))
    print("Final table state:", ht)

    # --- Basic Performance Benchmark ---
    print("\nInsert timing benchmark:\n")

    sizes = [100, 500, 1000, 2000, 5000]
    for size in sizes:
        ht = HashTable(size=100)  # Keep table size fixed to simulate rising load factor
        start = time.perf_counter()
        for i in range(size):
            ht.insert(f"key{i}", i)
        end = time.perf_counter()
        print(f"Inserted {size:>5} elements in {end - start:.6f} seconds")
