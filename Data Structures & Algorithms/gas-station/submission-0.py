class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        for start in range(n):
            tank=0
            possible=True
            for j in range(n):
                idx=(start+j)%n
                tank+=gas[idx]
                tank-=cost[idx]
                if tank<0:
                    possible=False
                    break
            if possible:
                return start
        return -1
                