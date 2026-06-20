class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in range(len(points)):
            dist=math.sqrt(points[i][0]**2+points[i][1]**2)
            heap.append((dist,points[i]))
        heapq.heapify(heap)
        ans=[]
        while k>0:
            tup=heapq.heappop(heap)
            ans.append(tup[1])
            k-=1
        return ans

        
        