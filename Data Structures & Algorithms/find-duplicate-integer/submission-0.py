
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=0
        s=set()
        for right in range(len(nums)):
            if nums[right] in s:
                return nums[right]
            else:
                s.add(nums[right])
        