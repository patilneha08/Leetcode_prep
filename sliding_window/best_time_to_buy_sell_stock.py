class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        mx=0
        for r in range(len(prices)):
            mx=max(mx,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l=r
        return mx