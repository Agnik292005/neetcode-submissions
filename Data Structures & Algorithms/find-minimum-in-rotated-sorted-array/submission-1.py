class Solution:
    def findMin(self, nums: List[int]) -> int:
        mi=nums[0]
        start=0
        end=len(nums)
        high=nums[end-1]
        while(start<end):
            mid=start+(end-start)//2
            if nums[mid]<mi:
                mi=nums[mid]
            if nums[mid]>high:
                start=mid+1
            else:
                end=mid
        return mi
                
        