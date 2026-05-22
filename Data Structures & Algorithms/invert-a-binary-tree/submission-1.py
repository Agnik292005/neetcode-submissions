class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return
            
            invert(node.left)
            invert(node.right)
            node.left, node.right = node.right, node.left
            return node
        return invert(root)