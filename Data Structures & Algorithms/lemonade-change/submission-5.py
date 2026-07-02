class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        twenties=0
        for i in bills:
            if i==5:
                fives+=1
            elif i==10:
                tens+=1
                if fives<=0:
                    return False
                else:
                    fives-=1
            elif i==20:
                twenties+=1
                if tens<=0 and fives<=0:
                    return False
                elif fives>0 and tens>0:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
                
        return True