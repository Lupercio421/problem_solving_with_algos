from NeetCode.Arrays_and_Hashing.DesignHashMap import Bucket

class MyHashMap:

    def __init__(self):
        self.key_space = 2069  # better to be a prime number, less collision
        self.hash_table = [Bucket() for i in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].update(key,value)

    def get(self, key: int) -> int:
        hash_key = key % self.key_space
        return self.hash_table[hash_key].get(key)

    def remove(self, key: int) -> None:
        # if not self.hash_table:
        #     del self.hash_table[key]
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)