class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1
        a=0
        
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        ans=set(s[0])
        while(right<len(s)):
            print(right,left)
            if s[right] in ans:
                ans.remove(s[left])
                left+=1
                
            else:
                ans.add(s[right])
                right+=1
            if a<right-left:
                a=right-left
        return a