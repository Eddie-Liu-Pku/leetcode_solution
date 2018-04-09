class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #注意这是个时间股票序列，维持时间序列
        min_price=2**31-1
        max_price=0
        profit=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            if prices[i]-min_price>profit:
                profit=prices[i]-min_price
        return profit
            