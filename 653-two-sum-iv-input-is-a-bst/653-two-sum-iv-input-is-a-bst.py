# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        values = []
        
        def travel(root: Optional[TreeNode]):
            if not root:
                return
            
            travel(root.left)
            values.append(root.val)
            travel(root.right)
            
        travel(root)
        
        values = set(values)
        for value in list(values):
            values.remove(value)
            if k-value in values:
                return True
            values.add(value)
        return False