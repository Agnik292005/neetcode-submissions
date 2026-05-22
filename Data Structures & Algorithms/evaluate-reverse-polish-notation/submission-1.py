class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if len(stack)>=2 and i in "+-/*":
                op2=int(stack.pop())
                op1=int(stack.pop())
                if i=="+":
                    res=op1+op2
                    stack.append(res)
                elif i=="*":
                    res=op1*op2
                    stack.append(res)
                elif i=="-":
                    res=op1-op2
                    stack.append(res)
                else :
                    res=int(op1/op2)
                    stack.append(res)
            else:
                stack.append(i)
        return int(stack[-1])

        