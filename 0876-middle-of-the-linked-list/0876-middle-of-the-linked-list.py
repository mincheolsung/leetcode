# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 0
        cur = head
        while cur:
            cur = cur.next
            len+=1
            
        len //= 2
        cur = head
        while cur and len > 0:
            cur = cur.next
            len -= 1

        return cur