class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            elif i in "+-*/" and len(stack)>=2:
                a=stack.pop()
                b=stack.pop()
                if i=="+":
                    result=int(a)+int(b)
                elif i=="/":
                    result=int(int(b)/int(a))
                elif i=="-":
                    result=int(b)-int(a)
                elif i=="*":
                    result=int(a)*int(b)
                stack.append(result)
        return int(stack[-1])
        