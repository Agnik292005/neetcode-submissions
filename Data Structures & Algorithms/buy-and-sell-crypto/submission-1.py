class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        ans=[0]*len(prices)
        for i in range(len(prices)):
            if prices[i]<m:
                m=prices[i]
            ans[i]=m
        mx=0
        for i in range(len(prices)):
            if prices[i]-ans[i]>mx:
                mx=prices[i]-ans[i]
        return mx

        