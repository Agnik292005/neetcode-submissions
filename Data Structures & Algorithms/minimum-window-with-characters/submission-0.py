class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need={}
        reslen=float("inf")
        res=[-1,-1]
        for i in t:
            need[i]=need.get(i,0)+1
        left=0
        have=0
        window={}
        required=len(need)
        for right in range(len(s)):
            c=s[right]
            window[c]=window.get(c,0)+1
            if c in need and window[c]==need[c]:
                have+=1
            while have==required:
                if right-left+1<reslen:
                    reslen=right-left+1
                    res=[left,right]
                
                window[s[left]]=window.get(s[left],0)-1
                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1
                left+=1
                
                
                
                
        return s[res[0]:res[1]+1]
            


        