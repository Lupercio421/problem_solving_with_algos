class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        hash_key = self.hash_function(key)
        node = self.table[hash_key]

        if not node:
            self.table[hash_key] = Node(key, value)
            self.size += 1
        
        else:
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1
        
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        hash_key = self.hash_function(key)
        node = self.table[hash_key]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        hash_key = self.hash_function(key)
        node = self.table[hash_key]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[hash_key] = node.next
                self.size -=1
                return True
            prev,node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity

        for node in self.table:
            while node:
                hash_key = node.key % self.capacity
                if new_table[hash_key] is None:
                    new_table[hash_key] = Node(node.key, node.value)
                else:
                    new_node = new_table[hash_key]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next
        self.table = new_table

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
