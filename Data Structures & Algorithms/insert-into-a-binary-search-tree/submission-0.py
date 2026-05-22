# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans=root
        add=TreeNode(val=val)
        if not root:
            return add
        while(root):
            if val<root.val:
                if not root.left:
                    root.left=add
                    break
                else:
                    root=root.left
                    continue
            else:
                if not root.right:
                    root.right=add
                    break
                else:
                    root=root.right
                    continue
        return ans
                

        