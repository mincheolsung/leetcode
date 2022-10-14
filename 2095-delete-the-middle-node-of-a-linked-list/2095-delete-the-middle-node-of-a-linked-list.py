# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
            
        if n == 1:
            return None
        
        target = n//2
        
        current = head
        while current and target > 0:
            target -= 1
            prev = current
            current = current.next
            
        prev.next = current.next
        
        return head
            