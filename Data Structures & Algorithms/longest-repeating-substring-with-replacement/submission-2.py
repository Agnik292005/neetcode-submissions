class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}
        left=0
        m=0
        max_wind_size=0
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]]=1
            else:
                freq[s[right]]+=1
            if m<freq[s[right]]:
                m=freq[s[right]]
            if right-left+1-m<=k:
                pass
            else: 
                while(right-left+1-m>k):
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        freq.pop(s[left])
                    left+=1
                
            if max_wind_size<right-left+1:
                max_wind_size=right-left+1
        return max_wind_size
            
        