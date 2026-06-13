# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        n1=list1
        n2=list2
        while n1 and n2:
            if n1.val<n2.val:
                curr.next=n1
                n1=n1.next
            else:
                curr.next=n2
                n2=n2.next
            curr=curr.next
        if n1:
            curr.next = n1
        else:
            curr.next = n2
        return dummy.next