# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def merge2(self,head1,head2):
        dummy=ListNode(0)
        cur=dummy
        while head1 and head2:
            if head1.val>head2.val:
                cur.next=head2
                head2=head2.next
            else:
                cur.next=head1
                head1=head1.next
            cur=cur.next
        if head1:
            cur.next=head1
        if head2:
            cur.next=head2
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        n=len(lists)
        cur=None
        for i in lists:
            cur=self.merge2(cur,i)

        return cur
        