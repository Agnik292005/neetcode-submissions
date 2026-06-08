class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(key=lambda x: x[0],reverse=True)
        time=[]
        for i in range(len(speed)):
            time.append((target-cars[i][0])/(cars[i][1]))
        
        if len(time)==1:
            return 1   
        fleets=1     
        fleettime=time[0]
        for i in range(1,len(time)):
            if time[i]<=fleettime:
                continue
            else:
                fleets+=1
                fleettime=time[i]

        print(*time)
        return fleets