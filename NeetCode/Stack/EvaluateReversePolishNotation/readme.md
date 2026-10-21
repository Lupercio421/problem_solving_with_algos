# [Problem/Topic Title]

[Brief description of the concept or problem]

## Intuition

[Explain your initial approach and thought process]

## Approach

[Detailed steps of your solution strategy]

1. a
    - b
2. c
    - d
        - e

## Complexity

- Time complexity: O(?)
- Space complexity: O(?)

## Code

<details>

<summary>Java - Stack attempt 1</summary>

```java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> rpnStack = new Stack<>();
        for (String token : tokens) {
            switch (token) {
                case ("+"):
                    int operand1 = (rpnStack.pop());
                    int operand2 = (rpnStack.pop());
                    rpnStack.push(operand2 + operand1);
                    break;
                case ("*"):
                    int value1 = (rpnStack.pop());
                    int value2 = (rpnStack.pop());
                    rpnStack.push(value2 * value1);
                    break;
                case ("-"):
                    int firstPopped = rpnStack.pop();
                    int secondPopped = rpnStack.pop();
                    rpnStack.push(secondPopped - firstPopped);
                    break;
                case ("/"):
                    int firstOperand = rpnStack.pop();
                    int secondOperand = rpnStack.pop();
                    rpnStack.push(secondOperand / firstOperand);
                    break;
                default:
                    int singleToken = Integer.parseInt(token);
                    rpnStack.push(singleToken);
                    break;
            }
        }
        return rpnStack.pop();
    }
}
```
</details>

<details>

<summary>Java - Stack attempt 2</summary>

```java
class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        for (String c : tokens) {
            if (c.equals("+")) {
                stack.push(stack.pop() + stack.pop());
            } else if (c.equals("-")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b - a);
            } else if (c.equals("*")) {
                stack.push(stack.pop() * stack.pop());
            } else if (c.equals("/")) {
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b / a);
            } else {
                stack.push(Integer.parseInt(c));
            }
        }
        return stack.pop();
    }
}
```
</details>


<details>


<summary>Python - attempt 1</summary>

```python
class Solution: 
```
</details>

## Notes

[Any additional notes or alternative approaches]
