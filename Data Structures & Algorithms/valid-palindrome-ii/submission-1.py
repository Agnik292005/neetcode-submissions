def isPalindrome(l,r,s):
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start=0
        end=len(s)-1

        while(start<=end):
            if s[start]==s[end]:
                start+=1
                end-=1
            else:
                if isPalindrome(start+1,end,s):
                    return True
                elif isPalindrome(start,end-1,s):
                    return True
                else:
                    return False
        if start>end:
            return True
        return False
            
 
        