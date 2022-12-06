# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()

        cur = head
        curOdd = odd
        curEven = even
        idx = 0
        while cur:
            idx+=1
            if idx % 2 == 1:
                curOdd.next = cur
                curOdd = cur
            else:
                curEven.next = cur
                curEven = cur
            cur = cur.next

        curOdd.next = even.next
        curEven.next = None
        return odd.next