class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for start, end in intervals:
            if newInterval and end<newInterval[0]:
                ans.append([start,end])
            elif newInterval and newInterval[1]<start:
                ans.append(newInterval)
                ans.append([start,end])
                newInterval=None
            elif newInterval:
                newInterval[0]=min(newInterval[0],start)
                newInterval[1]=max(newInterval[1],end)
            else:
                ans.append([start,end])
        if newInterval:
            ans.append(newInterval)
        return ans


    
        