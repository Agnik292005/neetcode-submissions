# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one=list1
        two=list2
        ans=ListNode(0)
        ans_head=ans
        while one is not None and two is not None:
            if one.val<=two.val:
                ans.next=ListNode(one.val)
                one=one.next
                ans=ans.next
            else:
                ans.next=ListNode(two.val)
                two=two.next
                ans=ans.next
        if one is None:
            while two is not None:
                ans.next=ListNode(two.val)
                two=two.next
                ans=ans.next
        elif two is None:
            while one is not None:
                ans.next=ListNode(one.val)
                one=one.next
                ans=ans.next

        
        return ans_head.next
        