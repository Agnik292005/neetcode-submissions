class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]>nums2[j]:
                res.append(nums2[j])
                j+=1
            else:
                res.append(nums1[i])
                i+=1
        if i<len(nums1):
            while i<len(nums1):
                res.append(nums1[i])
                i+=1
        elif j<len(nums2):
            while j<len(nums2):
                res.append(nums2[j])
                j+=1
        if len(res)%2==0:
            return (res[len(res)//2-1]+res[len(res)//2])/2
        else:
            return res[len(res)//2]
        
        