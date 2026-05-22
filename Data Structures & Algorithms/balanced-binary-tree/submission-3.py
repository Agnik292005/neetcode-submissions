# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.m=True
        def dfs(node):
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            return 1+max(left,right)
        def Balance(node):
            if not node:
                return True
            if abs(dfs(node.left)-dfs(node.right))>1:
                return False
            return Balance(node.left) and Balance(node.right)
        return Balance(root)
        