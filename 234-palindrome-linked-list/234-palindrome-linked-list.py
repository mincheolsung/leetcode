# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l = []
        length = 0
        cur = head
        while cur:
            length+=1
            l.append(cur.val)
            cur = cur.next
            
        left = 0
        right = length-1
        
        while left < right:
            if l[left] != l[right]:
                return False
            left+=1
            right-=1
            
        return True