class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        end=len(nums)-1
        res=-1
        while(start<=end):
            mid=start+(end-start)//2
            if(nums[mid]==target):
                res=mid
                return res
            if(nums[mid]>=nums[start]):
                #left side is sorted
                if(target>=nums[start] and target<nums[mid]):
                    end=mid-1
                else:
                    start=mid+1
            else:
                #right side is sorted
                if(target>nums[mid] and target<=nums[end]):
                    start=mid+1
                else:
                    end=mid-1
        return res
        
        