class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_price = prices[0]

        for x in prices:
            min_price = min(min_price, x)
            maxP = max(maxP, x-min_price)
        return maxP



        