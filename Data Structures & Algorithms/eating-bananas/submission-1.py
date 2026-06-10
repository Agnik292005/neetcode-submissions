class Solution:
    def can_finish(self,a,arr,h):
        hours=0
        for i in arr:
            hours+=math.ceil(i/a)
        if hours<=h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minspd=1
        maxspd=max(piles)
        while minspd<=maxspd:
            mid=minspd+(maxspd-minspd)//2
            if self.can_finish(mid,piles,h):
                maxspd=mid-1
            else:
                minspd=mid+1
        return minspd
        