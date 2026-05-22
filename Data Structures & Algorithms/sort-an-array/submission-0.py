
def mergesort(arr,left,right):
    if left<right:
        mid=left+(right-left)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,right,mid)
    return arr


def merge(arr,left,right,mid):
    len1=mid-left+1
    len2=right-mid
    arr1=[0]*len1
    arr2=[0]*len2
    for i in range(len1):
        arr1[i]=arr[left+i]
    for j in range(len2):
        arr2[j]=arr[mid+j+1]
    i=0
    j=0
    k=left
    while(i<len1 and j<len2):
        if arr1[i]<=arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j+=1
        k+=1

    while(i<len1):
        arr[k]=arr1[i]
        i+=1
        k=k+1
    
    while(j<len2):
        arr[k]=arr2[j]
        j+=1
        k+=1


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        arr=mergesort(nums,left,right)
        return arr
        
        