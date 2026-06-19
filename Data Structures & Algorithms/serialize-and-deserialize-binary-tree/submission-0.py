# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s=[]
        def create(s,node):
            if not node:
                s.append('N')
                return s
            s.append(str(node.val))
            create(s,node.left)
            create(s,node.right)
            
            return s
        s=create(s,root)
        return ','.join(s)
        

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst=data.split(',')
        self.i=0
        def buildtree(lst):
            if lst[self.i]=='N':
                self.i+=1
                return None
            node=TreeNode(int(lst[self.i]))
            self.i+=1
            node.left=buildtree(lst)
            node.right=buildtree(lst)
            return node
        return buildtree(lst)

        

