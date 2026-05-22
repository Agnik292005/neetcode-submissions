class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=len(nums)
        ans=set()
        left=0
        right=0
        for i in range(l):
            if i-left>k:
                ans.remove(nums[left])
                left+=1
            if nums[i] not in ans:
                ans.add(nums[i])
            else:
                if(i-left<=k):
                    return True
        return False


                
        