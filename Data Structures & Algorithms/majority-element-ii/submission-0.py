class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        ans=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>n//3:
                ans.append(i)
        return ans