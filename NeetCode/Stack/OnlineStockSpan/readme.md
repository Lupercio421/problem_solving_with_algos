# Online Stock Span - Monotonic Decreasing Stack

Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The `span` of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was *less than or equal to the price of that day*.

For example, if the prices of the stock in the last four days is `[7,2,1,2]` and the price of the stock today is `2`, then the span of today is `4` because starting from today, the price of the stock was less than or equal `2` for `4` consecutive days.
Also, if the prices of the stock in the last four days is [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal 8 for 3 consecutive days.

Implement the `StockSpanner` class:

- `StockSpanner()` Initializes the object of the class.
- `int next(int price)` Returns the `span` of the stock's price given that today's price is price.

```
Input: ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output: [null, 1, 1, 1, 2, 1, 4, 6]
```

## Intuition

A stack would be helpful. A int value keeping track of the span will be increased, and at the same time, something from the stack will be popped

## Approach

[Detailed steps of your solution strategy]

1. Initialize an empty stack that stores pairs of `(price, span)`.
2. For each `next(price)` call:
    - Start with `span = 1` (counting today).
    - While the stack is not empty and the top price is less than or equal to the current price:
        - Pop the top element and add its span to the current span.
    - Push `(price, span)` onto the stack.
    - Return `span`.

## Complexity

- Time complexity: O(n)
- Space complexity: O(n)

## Code

<details>

<summary>Java</summary>

```java
class StockSpanner {
    
    private Stack<int[]> stack; //pair: [price, span]

    public StockSpanner() {
        stack = new Stack<>();
    }
    
    public int next(int price) {
        int span = 1; //default span value
        while (!stack.isEmpty() && stack.peek()[0] <= price){
            span += stack.pop()[1];
        }
        //when price is not less than or equal to those on the stack
        stack.push(new int[]{price, span});
        return span;
    }
}
```
</details>

<details>

<summary>Python</summary>

```python
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span
```
</details>

## Notes

[Any additional notes or alternative approaches]

