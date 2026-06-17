# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            return 1+max(dfs(node.left),dfs(node.right))
        def Bal(node):
            if not node:
                return True
            if Bal(node.left) and Bal(node.right):
                if abs(dfs(node.left)-dfs(node.right))<=1:
                    return True
            return False
        return Bal(root)