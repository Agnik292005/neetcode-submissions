class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        
        while(n!=1):
            sum=0
            while(n>0):
              last=n%10
              sum+=last**2
              n=n//10
            if sum==1:
                return True
            elif sum in visited:
                return False
            visited.add(sum)
            n=sum
        return True

        
        
            
            
        