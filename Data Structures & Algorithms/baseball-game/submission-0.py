class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for ch in operations:
            if ch=="+":
                if len(stack)>=2:
                    stack.append(int(stack[-1])+int(stack[-2]))
            elif ch=="C":
                if stack:
                    stack.pop()
            elif ch=="D":
                if stack:
                    stack.append(int(stack[-1])*2)
            else:
                stack.append(int(ch))
        s=0
        for i in stack:
            s+=i
        return s
        