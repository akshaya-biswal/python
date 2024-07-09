class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    # Computes the hash index for the given key
    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        # Initializes the list at the bucket if it's empty
        if self.table[index] is None:
            self.table[index] = []

        for pair in self.table[index]:
            # If key is found, update the value
            if pair[0] == key:
                pair[1] = value
                return
        # If key is not found, append the new key-value pair
        self.table[index].append([key, value])

    def delete(self, key):
        index = self._hash_function(key)
        # If the bucket is empty, key doesn't exist
        if self.table[index] is None:
            return

        for i, pair in enumerate(self.table[index]):
            # If key is found, delete the key-value pair
            if pair[0] == key:
                del self.table[index][i]
                return

    def search(self, key):
        index = self._hash_function(key)
        # If the bucket is empty, key doesn't exist
        if self.table[index] is None:
            return None

        for pair in self.table[index]:
            # If key is found, return the value
            if pair[0] == key:
                return pair[1]
        # If key is not found in the list
        return None

    # Update is same as insert in this case
    def update(self, key, value):
        self.insert(key, value)

    def display_table(self):
        for index, bucket in enumerate(self.table):
            print(f"Bucket {index}: {bucket}")


# Example Usage
hash_table = HashTable(10)
hash_table.insert("apple", 100)
hash_table.insert("banana", 200)
hash_table.insert("cherry", 300)
hash_table.insert("date", 400)
hash_table.insert("mango", 100)


print(hash_table.search("apple"))  # Output: 100
print(hash_table.search("banana"))  # Output: 200

hash_table.update("mango", 150)

hash_table.display_table()
