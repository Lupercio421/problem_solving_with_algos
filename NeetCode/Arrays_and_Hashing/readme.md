# Hash Usage & Hash Implementation

## What is a HashMap?
A `HashMap` (or hash table) is a data structure that stores key-value pairs and allows for fast retrieval, insertion, and deletion of values based on their keys. It uses a hash function to convert keys into indices in an underlying array, making operations efficient (typically `O(1)` time on average). Hashmaps are `NOT` ordered, it is not possible to traverse the keys of a hashmap in any particular order.

### How HashMap Works
- **Hash Function:** Converts a key into an array index. A hashable object is one whose hash values, returned by a `hash()` function, never changes in it's lifetime.
- **Buckets:** Each index points to a bucket that stores key-value pairs. Collisions (multiple keys mapping to the same index) are handled by chaining (linked lists) or open addressing.
- **Operations:**
  - **Insert:** Place the key-value pair in the bucket at the hashed index.
  - **Get:** Retrieve the value for a key by hashing and searching the bucket.
  - **Remove:** Delete the key-value pair from the bucket.

### Example from Provided Classes
- `HashTable` uses an array of linked lists (nodes) to handle collisions.
- `MyHashMap` uses an array of `Bucket` objects, each storing a list of key-value pairs.
- `Bucket` class manages the key-value pairs for each hash index.

## What Makes a Good Hash Implementation?
1. **Efficient Hash Function:**
   - Should distribute keys uniformly across the array or storage space, to minimize collisions.
   - Example: `key % capacity` (as in `HashTable` and `MyHashMap`).
   - Using a prime number for capacity (like `2069` in `MyHashMap`) helps reduce clustering.
2. **Collision Handling:**
   - Chaining (linked lists or arrays in buckets) or open addressing.
   - The classes use chaining: `Node` linked lists in `HashTable`, lists in `Bucket`.
3. **Dynamic Resizing:**
   - When the load factor (size/capacity) gets too high, resize the table to maintain efficiency.
   - `HashTable` doubles its capacity when half full.
4. **Fast Operations:**
   - Insert, get, and remove should be O(1) on average.
   - The implementations achieve this with good hash functions and collision handling.

## Best Practices
- Use immutable and hashable keys (integers, strings).
- Choose a good initial capacity and resize policy.
- Handle collisions gracefully.
- Avoid high load factors to keep operations fast.

## References to The Code
- `HashTable.insert`, `get`, `remove`, and `resize` show classic hash table operations.
- `MyHashMap` and `Bucket` demonstrate modular design and collision handling.

---
**Summary:**
A HashMap is a powerful data structure for fast key-value storage. Good hash implementations use efficient hash functions, handle collisions, and resize dynamically to maintain performance. The provided classes are solid examples of these principles in Python.
