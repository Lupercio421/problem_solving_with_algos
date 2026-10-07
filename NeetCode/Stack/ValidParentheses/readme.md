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

<summary>Java attempt 1</summary>

```java
public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> closeToOpen = new HashMap<>();
        closeToOpen.put(')', '(');
        closeToOpen.put(']', '[');
        closeToOpen.put('}', '{');

        for (char c : s.toCharArray()) {
            if (closeToOpen.containsKey(c)) {
                if (!stack.isEmpty() && stack.peek() == closeToOpen.get(c)) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c); //this would trigger when there is a unclosable bracket and the "return false" would be returned
            }
        }
        return stack.isEmpty(); //instead of returning an explicit true. use the isEmpty() method to ensure it is empty / true
    }
}
```
</details>


## Notes

[Any additional notes or alternative approaches]
