class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        s=0
        MIN=100000000000
        count=0
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                if right-left+1<MIN:
                    MIN=right-left+1
                s-=nums[left]
                left+=1
        if MIN==100000000000:
            return 0
        return MIN
            

        