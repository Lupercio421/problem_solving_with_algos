# Implement Stack Using Queues - Queues and LinkedLists

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:

- `void push(int x)` Pushes element `x` to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns true if the stack is empty, false otherwise.

`Notes`:

- You must use **only** standard operations of a queue, which means that only `push` to `back`, `peek/pop from front`, `size` and `is empty` operations are valid.

- Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

```text
Example 1:

Input: ["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]

Output: [null, null, null, 2, 2, false]

Explanation:
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
```

## Intuition - Using Two Queues

Queue - follows First-In-First-Out
Stack - follows Last-In-First-Out.

To simulate a stack using queues, we need to reverse the order of elements on each push.
The idea is to two queues: when pushing a new element, we add it to the empty second queue, then move all elements from the first queue behind it. This places the newest element at the front, ready to be popped first.
After rearranging, we swap the two queues so the main queue always has elements in stack order.

## Approach - Using Two Queues

1. Initialize two empty queues `q1` and `q2`.
2. `push(x)`: Add `x` to `q2`, then move all elements from `q1` to `q2` one by one. Finally swap `q1` and `q2`. 
3. `pop()`: Remove and return the front element from `q1`.
4. `top()`: Return the front element of `q1` without removing it.
5. `empty()`: Return `true` if `q1` is empty.

## Complexity - Using Two Queues

- Time complexity: 
    - O(1) time for initialization
    - O(n) time for each *push()* function call.
    - O(1) time for each *pop()* function call.
- Space complexity: O(n)

## Code - Using Two Queues

<details>

<summary>Java - Using Two Queues</summary>

```java
class MyStack {
    Queue<Integer> queueA;
    Queue<Integer> queueB;
    
    public MyStack() {
        queueA = new LinkedList<>();
        queueB = new LinkedList<>();
    }
    
    public void push(int x) {
        queueB.offer(x);
        while (!queueA.isEmpty()){
            queueB.offer(queueA.poll());
        }
        Queue<Integer> temp = queueA;
        queueA = queueB;
        queueB = temp;
    }
    
    public int pop() {
        return queueA.poll();
    }
    
    public int top() {
        return queueA.peek();
    }
    
    public boolean empty() {
        return queueA.isEmpty();
    }
}
```
</details>

<details>

<summary>Python - Using Two Queues </summary>

```python
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0
```
</details>

## Intuition - Using One Queue

The `pop`, `top` and `empty` methods will have the same functionality as the double queue solution. This approach differs in that the new element will be added to the queue and the same queue will be rotated to that the newest element moves to the front. When we add an element, we push it to the back of the queue, then dequeue and re-enqueue all the elements that were already there. This effectively moves the new element to the front.

## Approach - Using One Queue

1. Initialize a single empty queue `q`.
2. `push(x)`: Add `x` to `q`. Then rotate the queue by removing and re-adding elements of `size - 1`. This moves `x` to the front. 
3. `pop()`: Remove and return the front element from `q`.
4. `top()`: Return the front element of `q` without removing it.
5. `empty()`: Return `true` if `q` is empty.

- Time complexity: 
    - O(1) time for initialization
    - O(n) time for each *push()* function call.
    - O(1) time for each *pop()* function call.
- Space complexity: O(n)

## Code - Using One Queue

<details>

<summary>Java - Using One Queue </summary>

```java
class MyStack {
    Queue<Integer> queueA;
    public MyStack() {
        queueA = new LinkedList<>();
    }

    public void push(int x) {
        queueA.offer(x);
        for (int i = queueA.size() - 1; i > 0; i--) {
            queueA.offer(queueA.poll());
        }
    }

    public int pop() {
        return queueA.poll();
    }

    public int top() {
        return queueA.peek();
    }

    public boolean empty() {
        return queueA.isEmpty();
    }
}
```
</details>

<details>

<summary>Python - Using One Queue </summary>

```python
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
```

</details>

## Intuition - Queue of Queues

This approach takes a different perspective by nesting structures. Instead of rearranging elements, we create a new queue (or node) for each push that contains the value and a reference to the previous structure.

Each push wraps the current state inside a new container, with the new value at the front. This creates a chain where the most recent element is always immediately accessible.

In practice, this behaves like building a linked list where each node holds a value and points to the rest of the stack.

## Approach - Queue of Queues

1. Initialize `q` as `null` (empty stack).
2. `push(x)`: Create a new queue/node containing `x` as the first element and the old `q` as the second element. Update `q` to point to this new structure.
3. `pop()`: Extract the first element (the value), update `q` to point to the second element (the rest of the stack), and return the value.
4. `top()`: Return the first element of `q` without modifying anything.
5. `empty()`: Return `true` if `q` is `null`.

## Code - Queue of Queues.

<details>

<summary>Java - Queue of Queues/summary>

```java
class MyStack {

    private Queue<Object> q;

    public MyStack() {
        q = null;
    }
    
    public void push(int x) {
        Queue<Object> newQueue = new LinkedList<>();
        newQueue.add(x);
        newQueue.add(q);
        q = newQueue;
    }
    
    public int pop() {
        if (q == null){
            return -1;
        }

        int top = (int) q.poll();
        q = (Queue<Object>) q.poll(); // the old stack is buried inside the current one, and popping/polling digs it back out
        return top;
    }
    
    public int top() {
        if (q == null) {
            return -1;
        }

        return (int) q.peek();
    }
    
    public boolean empty() {
        return q == null;
    }
}
```
</details>

<details>

<summary>Python - Queue of Queues</summary>

```python
class MyStack:

    def __init__(self):
        self.q = None

    def push(self, x: int) -> None:
        self.q = deque([x, self.q])

    def pop(self) -> int:
        top = self.q.popleft()
        self.q = self.q.popleft() #the old stack is buried inside the current one, and popping/polling digs it back out
        return top

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
```
</details>
