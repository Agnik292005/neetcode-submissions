class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st={}
        stt={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in st:
                st[s[i]]+=1
            else:
                st[s[i]]=1
        for i in range(len(t)):
            if t[i] in stt:
                stt[t[i]]+=1
            else:
                stt[t[i]]=1
        for c in st:
            if c in t and st[c]==stt[c]:
                continue
            else:
                return False
        return True