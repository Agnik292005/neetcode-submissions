class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur=intervals[0]
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=cur[1]:
                cur[0]=min(intervals[i][0],cur[0])
                cur[1]=max(intervals[i][1],cur[1])
            elif intervals[i][0]>cur[1]:
                ans.append(cur)
                cur=intervals[i]
        ans.append(cur)
        return ans
                
        