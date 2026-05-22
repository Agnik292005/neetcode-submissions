# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def gcd(num1,num2):
    while(num2!=0):
        q=num1//num2
        r=num1%num2
        num1=num2
        num2=r
    return num1
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        if head.next is None:
            return head
        ahead=head.next
        while start is not None and ahead is not None:
            middle=gcd(start.val,ahead.val)
            temp=start.next
            start.next=ListNode(middle)
            start.next.next=ahead
            start=ahead
            ahead=ahead.next
        return head