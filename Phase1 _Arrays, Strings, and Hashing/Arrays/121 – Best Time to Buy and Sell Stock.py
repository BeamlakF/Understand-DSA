class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):                  # buying day
            for j in range(i + 1, n):       # selling day
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

# The above was Brute force approach, and time limit exceeded for large inputs on Leetcode