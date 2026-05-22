# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start1=l1
        start2=l2
        carry=0
        s=0
        dummy=ListNode(0)
        head=dummy
        while(start1 is not None or start2 is not None or carry):
            val1 = start1.val if start1 else 0
            val2 = start2.val if start2 else 0

            s = val1 + val2 + carry

            dummy.next=ListNode((s)%10)
            carry=s//10
            if start1:
                start1=start1.next
            if start2:
            
                start2=start2.next
            dummy=dummy.next
        return head.next
        