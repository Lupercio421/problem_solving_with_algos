# Perfect Squares - Dynamic Programming

You are given an integer `n`, return the least number of perfect square numbers that sum to `n`.

A `perfect square` is an integer that is the square of an integer. For example, 1, 4, 9, 16, 25... are perfect squares.

```text
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9
```

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

### Python

```python
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if target - square < 0:
                    break
                dp[target] = min(dp[target], 1 + dp[target - square])
        
        return dp[n]
```

### Java

```java
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n);
        dp[0] = 0;

        for (int target = 1; target <= n; target++){
            for (int s = 1; s * s <= target; s++){
                dp[target] = Math.min(dp[target], 1 + dp[target - s * s]);
            }
        }
    return dp[n];
    }
}
```

## Notes

[Any additional notes or alternative approaches]
