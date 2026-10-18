# Min Stack - Stack

Design a stack class that supports the push, pop, top, and getMin operations.

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.

## Intuition

The most recognizable solution would be to use two stacks. One serving as the primary stack, the other serving as a minimum stack holding the minimum value across all values. The top of the minimum stack will always hold the minimum of the entire primary stack. Allowing for O(1) retrieval of the minimum value.

## Approach - Two Stacks

[Detailed steps of your solution strategy]

1. Maintain two stacks:
    - `stack` -> stores all pushed values.
    - `minStack` -> stores the minimum so far at each level.
2. On `push(val)`:
    - Push the `val` onto `stack`
    - Check if the `minStack` is empty
        - if it is, push the `val`
        - else, push the minimum between the top value from `minStack` or the current `val`.
3. On `pop()`:
    - Pop from both `stack` and `minStack` to keep them aligned
4. On `top()`:
    - Return the top of `stack`
5. On `getMin()`:
    - Return the top of `minStack()`, it is the current minimum

## Complexity

- Time complexity: O(1) for all operations
- Space complexity: O(n)

## Code

<details>

<summary>Java - Two Stacks</summary>

```java
class MinStack {
    public Stack<Integer> stack1;
    public Stack<Integer> minStack;

    public MinStack() {
        stack1 = new Stack<>();
        minStack = new Stack<>();
    }

    public void push(int val) {
        Integer minVal;
        stack1.push(val);

        if (minStack.isEmpty()) {
            minStack.push(val);
        } else {
            minVal = Math.min(minStack.peek(), val);
            minStack.push(minVal);
        }
    }

    public void pop() {
        stack1.pop();
        minStack.pop();
    }

    public int top() {
        return stack1.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}
```
</details>

<details>

<summary>Python - Two Stacks</summary>

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]

```
</details>

## Intuition - One Stack

## Approach - One Stack

## Code - One Stack

<details>

<summary>Java - One Stack</summary>

```java
class MinStack {
    public Stack<Long> stack;
    public long minVal;
    public MinStack() {
        stack = new Stack<>();
    }

    public void push(int val) {
        if (stack.isEmpty()) {
            stack.push(0L);
            minVal = val;
        } else {
            stack.push(val - minVal); // encoded value
            if (val < minVal) {
                minVal = val;
            }
        }
    }

    public void pop() {
        if (stack.isEmpty()) return;
        long pop = stack.pop();
        if (pop < 0){
            minVal = minVal - pop;
        }
    }

    public int top() {
        long top = stack.peek();
        if (top > 0) {
            return (int) (top + minVal); // decoded value
        } else {
            return (int) minVal;
        }
    }

    public int getMin() {
        return (int) minVal;
    }
}
```
</details>

<details>

<summary>Python - One Stack</summary>

```python
class MinStack:
    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
```
</details>


## Notes
