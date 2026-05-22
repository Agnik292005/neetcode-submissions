# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        slow=head
        fast=head
        while(fast is not None and fast.next is not None and fast.next.next is not None):
            fast=fast.next.next
            slow=slow.next
        #disconnect second half starting from slow.next
        second_head=slow.next
        slow.next=None
        #reverse second half
        prev=None
        cur=second_head
        while cur is not None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            
        second_head=prev
        first_head=head
        #merge the two lists alternately
        while second_head is not None and first_head is not None:
            temp1=first_head.next
            temp2=second_head.next
            first_head.next=second_head
            second_head.next=temp1
            first_head=temp1
            second_head=temp2