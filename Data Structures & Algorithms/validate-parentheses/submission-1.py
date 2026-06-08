class Solution:
    def isValid(self, s: str) -> bool:
        ref={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack[-1]!=ref[i]:
                    return False
                stack.pop()
        return len(stack)==0