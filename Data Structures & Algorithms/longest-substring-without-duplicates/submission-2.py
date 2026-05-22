class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1
        a=0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        while(right<len(s)):
            print(right,left)
            if s[right] in s[left:right]:
                left+=1
            else:
                right+=1
            if a<right-left:
                a=right-left
        return a