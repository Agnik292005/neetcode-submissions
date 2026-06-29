class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end=len(nums)-1
        farthest=0
        for i in range(len(nums)):
            if farthest==end:
                return True
            if i<=farthest:
                if nums[i]+i>farthest:
                    farthest=nums[i]+i
        print(farthest)
        if farthest>=end:
            return True
        return False

        