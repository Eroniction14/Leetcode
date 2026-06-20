class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=1
        a=0
        while (sell < len(prices)):
            if prices[buy]>prices[sell]:
                buy=sell                
            else:
                b=prices[sell]-prices[buy]
                if a<b:
                    a=b
            sell+=1
        return a
