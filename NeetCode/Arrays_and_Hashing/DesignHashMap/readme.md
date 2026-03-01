# Design HashMap - Chaining

Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

* `MyHashMap()` initializes the object with an empty map.
* `void put(int key, int value)` inserts a `(key, value)` pair into the HashMap. If the `key` already exists in the map, update the corresponding `value`.
* `int get(int key)` returns the `value` to which the specified key is mapped, or `-1` if this map contains no mapping for the `key`.
* `void remove(key)` removes the `key` and its corresponding `value` if the map contains the mapping for the `key`.

## Intuition

To reduce memory usage, we use a hash table with seperate chaining. We create an array of buckets (smaller than the key range) and use a hash function (key modulo bucket count) to determine which bucket a key belongs to. Each bucket is a linked list that stores key-value pairs. This handles collisions by chaining multiple entries in the same bucket.

## Approach

1. Initialize an array of `1000` buckets, each containing a dummy head node for a linked list.
2. Define a `hash(key)` method as `key % 1000`, where 1000 is the length of the array.
3. For `put(key, value)`: Traverse the linked list at `hash(key)`. Name this variable as `cur`. Because `cur` itself is a dummy `ListNode`, begin the node checking on `cur.next`. If a node with the matching key exists, update its value. Otherwise, return append a new node with the key-value pair.
4. For `get(key)`: Traverse the linked list at `hash(key)`. As described above, we can begin the node checking at `cur.next`. If a node with the matching `key` is found, return its value. Otherwise, return `-1`.
5. For `remove(key)`: Traverse the linked list at `hash(key)`. If a node with the matching key is found, remove it by updating the previous node's `next` pointer.

## Complexity

* Time complexity: O(?)
* Space complexity: O(?)

## Code

### Python

```python
class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]

    def hash(self, key):
        return key % len(self.map) #len of self.map is 1000

    def put(self, key: int, value: int) -> None:
        cur = self.map[self.hash(key)]
        #cur begins at dummny node. begin the checking at the next key
        while cur.next:
            if cur.next.key == key: #key already exists
                cur.next.val = value
                return
            cur = cur.next
        # we can insert a new ListNode() becuase cur.next is null
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        #start at the next node b/c cur is initialized at the dummy node
        cur = self.map[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        # we didn't find the key
        return -1
        

    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
```

### Java

```java
class ListNode{
    int key, val;
    ListNode next;

    public ListNode(int key, int val, ListNode next){
        this.key = key;
        this.val = val;
        this.next = next;
    }

    public ListNode(){
        this(-1, -1, null);
    }
}

class MyHashMap {

    private ListNode[] map;

    public MyHashMap() {
        map = new ListNode[1000];
        for (int i = 0; i < 1000; i++){
            map[i] = new ListNode();
        }
    }

    private int hash(int key){
        return key % map.length;
    }
    
    public void put(int key, int value) {
        ListNode cur = map[hash(key)];
        while (cur.next != null){
            if (cur.next.key == key){
                cur.next.val = value;
                return;
            }
            cur = cur.next;
        }
        cur.next = new ListNode(key, value, null);
    }
    
    public int get(int key) {
        ListNode cur = map[hash(key)].next;
        while (cur != null){
            if (cur.key == key){
                return cur.val;
            }
            cur = cur.next;
        }
        return -1;
    }
    
    public void remove(int key) {
        ListNode cur = map[hash(key)];
        while (cur.next != null){
            if (cur.next.key == key){
                cur.next = cur.next.next;
                return;
            }
            cur = cur.next;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
```

## Notes

* Multiple keys will be mapped to the same index. Nodes containing `key` and `value` will be chained together on the key of the `Array`
* ToDo: Research open addressing solution.
