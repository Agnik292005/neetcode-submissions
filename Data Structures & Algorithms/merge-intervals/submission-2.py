class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        intervals.sort()
        cur=intervals[0]
        if len(intervals)==1:
            ans.append(cur)
            return ans
        for i in range(1,len(intervals)):
            if cur[1]>=intervals[i][0]:
                cur[0]=min(intervals[i][0],cur[0])
                cur[1]=max(intervals[i][1],cur[1])
            else:
                ans.append(cur)
                cur=[intervals[i][0],intervals[i][1]]
        ans.append(cur)
        return ans