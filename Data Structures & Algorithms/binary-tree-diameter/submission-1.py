# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.m=0
        def path(node):
            if not node:
                return 0
            leftlen=path(node.left)
            rightlen=path(node.right)
            self.m=max(self.m,leftlen+rightlen)
            return 1+max(leftlen,rightlen)
        path(root)
        return self.m

            

        