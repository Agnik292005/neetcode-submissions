class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=set()
        left=0
        right=0
        result=0
        for right in range(len(s)):
            while s[right] in ans:
                ans.remove(s[left])
                left+=1
            ans.add(s[right])
            result=max(right-left+1,result)
        return result
                