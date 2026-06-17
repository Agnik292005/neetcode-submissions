# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.curr=0
        self.ans=0
        def inorder(node,k):
            if not node:
                return 0
            inorder(node.left,k)
            self.curr+=1
            if self.curr==k:
                self.ans=node.val
                return self.ans
            
            inorder(node.right,k)
        inorder(root,k)
        return self.ans

