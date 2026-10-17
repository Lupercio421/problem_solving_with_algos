
# Implement Queue using Stacks

Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

Implement the MyQueue class:

- `void push(int x)` Pushes element `x` to the back of the queue.
- `int pop()` Removes the element from the front of the queue and returns it.
- `int peek()` Returns the element at the front of the queue.
- `boolean empty()` Returns `true` if the queue is empty, `false` otherwise.

## Intuition

## Approach - Using Two Stacks

Make use of two stacks, `stack1` and `stack2`. 

1. For `push`, push the element onto `stack1`.
2. For `pop`: Move all the elements except the `last` (`LIFO : d <- c <- b <- a`) from `stack1` to `stack2`. Pop the remaining element from `stack1` and save to a variable. Then move all the elements back from `stack2` to `stack1`. Return the saved variable
3. For `peek`, it will be same as `pop`, but instead of popping, just read the top element of `stack1` after moving elements.
4. For `empty`: Return `true` if `stack1` is empty.

## Complexity - Using Two Stacks 

- Time complexity: 
    - O(n) for each `pop()` and `peek()` function calls
    - O(1) time for each `push()`, `empty()` function calls. And O(1) time for initialization. 
- Space complexity: O(n)

## Code - Using Two Stacks

<details>

<summary>Java - Using Two Stacks</summary>

```java
class MyQueue {

    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }
    
    public void push(int x) {
        stack1.push(x);
    }
    
    public int pop() {
        while(stack1.size() > 1){
            stack2.push(stack1.pop());
        }
        int res = stack1.pop();
        while (!stack2.isEmpty()){
            stack1.push(stack2.pop());
        }
        return res;
    }
    
    public int peek() {
        while (stack1.size() > 1){
            stack2.push(stack1.pop());
        }
        int res = stack1.peek();
        while (!stack2.isEmpty()){
            stack1.push(stack2.pop());
        }
        return res;
    }
    
    public boolean empty() {
        return stack1.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```
</details>


## Notes

[Any additional notes or alternative approaches]
