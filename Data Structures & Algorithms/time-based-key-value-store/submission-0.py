class TimeMap:

    def __init__(self):
        self.mp={}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp:
            self.mp[key]=[]
        self.mp[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        lis=self.mp.get(key,[])
        for i in range(len(lis)-1,-1,-1):
            if lis[i][1]<=timestamp:
                return lis[i][0]
        return ""
