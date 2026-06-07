class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j=0
        ans=""
        while j<len(strs[0]):
            s=strs[0][j]
            for i in range(len(strs)):
                if j>=len(strs[i]) or strs[i][j]!=s:
                    return ans
            ans+=s
            j+=1
        return ans



                

        
        