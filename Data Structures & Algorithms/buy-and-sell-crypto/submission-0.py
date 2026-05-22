class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        m=prices[0]
        ans=[]
        a=0
        for right in range(len(prices)):
            if prices[right]<m:
                m=prices[right]
                left=right
            else:
                if(prices[right]-prices[left]>=a):
                    a=prices[right]-prices[left]
        return a
        