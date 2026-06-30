class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if n<0:
            for i in range(1,-n+1):
                ans=float(ans/x)
            return ans
        for i in range(1,n+1):
            ans=ans*x
        return ans