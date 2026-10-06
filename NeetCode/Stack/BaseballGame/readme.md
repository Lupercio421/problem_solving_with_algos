# Baseball Game - Stack

You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

Given a list of strings `operations`, where `operations[i]` is the ith operation you must apply to the record and is one of the following:

An integer `x`: Record a new score of `x`.

'+': Record a new score that is the sum of the previous two scores.

'D': Record a new score that is the double of the previous score.

'C': Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

```text
Example 1:

Input: ops = ["1","2","+","C","5","D"]

Output: 18

Explanation:

"1" - Add 1 to the record, record = [1].
"2" - Add 2 to the record, record = [1, 2].
"+" - Add 1 + 2 = 3 to the record, record = [1, 2, 3].
"C" - Invalidate and remove the previous score, record = [1, 2].
"5" - Add 5 to the record, record = [1, 2, 5].
"D" - Add 2 * 5 = 10 to the record, record = [1, 2, 5, 10].
The total sum is 1 + 2 + 5 + 10 = 18.
```

## Intuition

The original plan was to treat this problem using a combination of if statements. Case statements turned out to be better.

Depending on the `operation`, we will be popping, pushing, or storing variables from the stack's peek() method.

## Approach

[Detailed steps of your solution strategy]

1. Initialize an empty stack to store valid scores
2. For each operation:
    - If it's `+`, add the sum of the top two elements to the stack.
    - If it's `D`, add double to the top element to the stack.
    - If it's `C`, pop the element.
    - Otherwise, it's a number, so push it onto the stack.
3. Return the sum of all elements in the stack.

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

## Code

<details>

<summary>Java - Stack 1</summary>

```java
class Solution {
    public int calPoints(String[] operations) {
        List<Integer> scores = new ArrayList<>();

        for (String operation : operations) {
            switch (operation) {
                case "D" -> {
                    int previousScore = scores.get(scores.size() - 1);
                    scores.add(previousScore * 2);
                }
                case "+" -> {
                    int lastScore = scores.get(scores.size() - 1);
                    int secondLastScore = scores.get(scores.size() - 2);
                    scores.add(lastScore + secondLastScore);
                }
                case "C" -> scores.remove(scores.size() - 1);
                default -> scores.add(Integer.parseInt(operation));
            }
        }

        return scores.stream()
                .mapToInt(Integer::intValue)
                .sum();
    }
}
```
</details>

<summary>Java - Stack 2</summary>

```java
public class Solution {
    public int calPoints(String[] ops) {
        int res = 0;
        Deque<Integer> stack = new ArrayDeque<>();

        for (String op : ops) {
            switch (op) {
                case "+":
                    int previous = stack.pop();
                    int combined = previous + stack.peek();
                    stack.push(previous);
                    stack.push(combined);
                    res += combined;
                    break;

                case "D":
                    int doubled = 2 * stack.peek();
                    stack.push(doubled);
                    res += doubled;
                    break;

                case "C":
                    res -= stack.pop();
                    break;

                default:
                    int score = Integer.parseInt(op);
                    stack.push(score);
                    res += score;
                    break;
            }
        }

        return res;
    }
}
```
</details>

<details>

<summary>Python - Stack 1</summary>

```python
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
```
</details>

## Notes

[Any additional notes or alternative approaches]
