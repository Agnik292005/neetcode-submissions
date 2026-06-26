class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cur=intervals[0]
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<cur[1]:
                if intervals[i][1]<cur[1]:
                    cur=intervals[i]
                else:
                    cur=cur
            elif intervals[i][0]>=cur[1]:
                ans.append(cur)
                cur=intervals[i]
        ans.append(cur)
        print(*ans)
        if len(intervals)==len(ans):
            return 0
        return len(intervals)-len(ans)
                
        