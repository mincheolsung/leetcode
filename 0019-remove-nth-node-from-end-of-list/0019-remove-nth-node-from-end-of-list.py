# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prehead = ListNode(-1, head)
        
        first = second = prehead
        while first and n > 0:
            n-=1
            first = first.next
        
        while first.next:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return prehead.next