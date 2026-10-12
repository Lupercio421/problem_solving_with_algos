# Best Time to Buy and Sell Stock II - Arrays

You are given an integer array prices where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. However, you can buy it then immediately sell it on the `same day`. Also, you are allowed to perform any number of transactions but can hold `at most one` share of the stock at any time.

Find and return the `maximum` profit you can achieve.

## Greedy Approach

### Intuition - Greedy

It is best to capture every upward price movement. If the price of the stock goes up from day `i` to day `i + 1`, we can always "buy" on day `i` and "sell" on day `i + 1` to capture that profit.

### Approach - Greedy

1. Initialize a `profit` variable to `0`.
2. Iterate through the prices from day `1` to the last day.
3. If today's (`i`) price is higher than yesterday's price, add the difference to `profit`, as a running sum.
4. Return `profit`

### Complexity

- Time complexity: *O(n)*
- Space complexity: *O(1)*

### Code - Greedy

#### Java

```java
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;

        for (int i = 1; i < prices.length; i++){
            if (prices[i] > prices[i - 1]){
                profit += (prices[i] - prices[i-1]);
            }
        }
        return profit;
    }
}
```

#### Python

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
            
        return profit
```

## Notes

[Any additional notes or alternative approaches]
