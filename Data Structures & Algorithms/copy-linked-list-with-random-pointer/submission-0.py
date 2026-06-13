"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        old_to_new={None:None}
        while curr:
            old_to_new[curr]=Node(curr.val)
            curr=curr.next
        
        secpass=head
        while secpass:
            copy=old_to_new[secpass]
            copy.next=old_to_new[secpass.next]
            copy.random=old_to_new[secpass.random]
            secpass=secpass.next
        return old_to_new[head]
        
        