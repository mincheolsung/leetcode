# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        prev = head
        cur = head.next
        
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        head.next = None
        
        return prev