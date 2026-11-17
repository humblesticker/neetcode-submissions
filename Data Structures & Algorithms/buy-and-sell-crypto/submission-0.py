class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit

        
"""
test
[10,8,7,5,2]
price, buy, profit
10, 10, 0
8, 8, 0
2, 2, 0

is there anyway without stat?
yes you can only update buy and get profit based on the current price
only update if profit gets larger
"""