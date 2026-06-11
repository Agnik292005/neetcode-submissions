class TimeMap:

    def __init__(self):
        self.mp={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key]=[]
        self.mp[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        lis=self.mp.get(key,[])
        if len(lis)==0:
            return ""
        
        left=0
        right=len(lis)-1
        res=""
        while left<=right:
            mid=left+(right-left)//2
            if lis[mid][1]<=timestamp:
                res=lis[mid][0]
                left=mid+1
            else:
                right=mid-1
        return res
