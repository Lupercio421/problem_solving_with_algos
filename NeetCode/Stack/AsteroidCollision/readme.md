# Asteroid Collision - Stack

You are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


## Intuition

Collisions only happen when a right-moving asteroid [+] meets a left-moving  asteroid [-]. With a stack, we can process asteroid left to right. When we see a negative asteroid, it can only collide with positive asteroids already on the stack. We keep popping and comparing until either the new asteroid is destroyed, destroys all opposing asteroids, or there are no more collisions possible.

## Approach

1. Initialize a empty stack.
2. For each asteroid, if it's positive or the stack is empty or the top is negative, push it.
3. If the asteroid is negative and the top is positive, compare sizes:
    - If the top is smaller, pop it and continue checking.
    - If they're equal, pop the top and discard the current asteroid.
    - If the top is larger, discard the current asteroid.
4. After processing all asteroids, the stack contains the survivors

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

## Code

<details>

<summary>Java - Stack and Array Element comparison</summary>

```java
public class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int a : asteroids) {
            while (!stack.isEmpty() && a < 0 && stack.peek() > 0) { //keep checking until no more collisions with the current asteroid, and those already on the stack
                int diff = a + stack.peek(); //better than absolute value comparison
                if (diff < 0) {
                    stack.pop();
                } else if (diff > 0) {
                    a = 0;
                } else {
                    a = 0;
                    stack.pop();
                }
            }
            if (a != 0) {
                stack.add(a);
            }
        }
        return stack.stream().mapToInt(i -> i).toArray();
    }
}
```
</details>

<details>

<summary>Python - Array element comparison</summary>

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        j = -1

        for a in asteroids:
            while j >= 0 and asteroids[j] > 0 and a < 0:
                if asteroids[j] > abs(a):
                    a = 0
                    break
                elif asteroids[j] == abs(a):
                    j -= 1
                    a = 0
                    break
                else:
                    j -= 1
            if a:
                j += 1
                asteroids[j] = a

        return asteroids[:j + 1]
```
</details>

## Intuition - Without Stack

We can simulate the stack behavior using the input array itself. We maintain a pointer `j` that tracks the "top" of our virtual stack within the array. When collisions occur, we decrement `j` (like popping). Surviving asteroids are written to position `j + 1`. This gives us O(1) extra space while maintaining the same logic.

## Approach - Without Stack

1. Use pointer `j = -1` to represent an empty stack.
2. For each asteroid, handle collisions by comparing with asteroids[j] when both are in opposite directions.
3. If the current asteroid survives, increment `j` and store it at `asteroids[j]`.
4. If destroyed, skip storing it.
5. Return the subarray from index `0` to `j` (inclusive).

<details>

<summary>Java - Without Stack</summary>

```java
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        int n = asteroids.length;
        int j = -1;

        for (int a : asteroids) {
            while (j >= 0 && asteroids[j] > 0 && a < 0) {
                if (asteroids[j] + a > 0) {
                    a = 0;
                    break;
                } else if (asteroids[j] + a == 0) {
                    j--;
                    a = 0;
                    break;
                } else {
                    j--;
                }
            }
            if (a != 0) {
                asteroids[++j] = a;
            }
        }
        return Arrays.copyOfRange(asteroids, 0, j + 1);
    }
}
```
</details>

<details>

<summary>Python - Without Stack</summary>

```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        j = -1

        for a in asteroids:
            while j >= 0 and asteroids[j] > 0 and a < 0:
                if asteroids[j] > abs(a):
                    a = 0
                    break
                elif asteroids[j] == abs(a):
                    j -= 1
                    a = 0
                    break
                else:
                    j -= 1
            if a:
                j += 1
                asteroids[j] = a

        return asteroids[:j + 1]
```
</details>

## Notes

[Any additional notes or alternative approaches]