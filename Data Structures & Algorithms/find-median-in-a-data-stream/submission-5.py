class MedianFinder:

    def __init__(self):
        self.arr=[]
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr=sorted(self.arr)
        

    def findMedian(self) -> float:
        idx=len(self.arr)-1
        if len(self.arr)%2==0:
            return float(self.arr[idx//2]+self.arr[idx//2+1])/2
        return self.arr[idx//2]
        
        