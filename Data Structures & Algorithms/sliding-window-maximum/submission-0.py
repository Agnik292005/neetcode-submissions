class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        right=k-1
        ans=[]
        while right<len(nums):
            ans.append(max(nums[left:right+1]))
            left+=1
            right+=1
        return ans
        