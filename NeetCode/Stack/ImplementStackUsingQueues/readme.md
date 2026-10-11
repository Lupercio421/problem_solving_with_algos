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

```
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

## Code

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

## Intuition - Queues of Queues

