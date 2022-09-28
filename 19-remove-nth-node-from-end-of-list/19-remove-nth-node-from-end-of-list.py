# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:    
        vals = deque([])
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next
            
        del vals[-n]
        if not vals:
            return None
        
        cur = prev = head
        while vals:
            prev = cur
            cur.val = vals.popleft()
            cur = cur.next
        prev.next = None
        
        return head