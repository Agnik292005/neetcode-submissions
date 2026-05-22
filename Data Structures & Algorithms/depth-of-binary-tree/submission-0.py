# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            else:
                if node.right and node.left:
                    if depth(node.right)>depth(node.left):
                        return 1+depth(node.right)
                    else:
                        return 1+depth(node.left)
                elif node.right:
                    return 1+depth(node.right)
                else:
                    return 1+depth(node.left)
        return depth(root)
        