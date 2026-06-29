class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while columnNumber>0:
            columnNumber-=1
            cur=columnNumber%26
            ans=s[cur]+ans
            columnNumber=columnNumber//26
        return ans
        