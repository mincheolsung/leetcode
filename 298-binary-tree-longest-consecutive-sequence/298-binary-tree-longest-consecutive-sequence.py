# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        result = 0
        
        def travel(root: Optional[TreeNode], length: int):
            nonlocal result
            
            result = max(result, length)

            if root.left and root.left.val == root.val + 1:
                travel(root.left, length+1)
            elif root.left:
                travel(root.left, 1)
            
            if root.right and root.right.val == root.val + 1:
                travel(root.right, length+1)
            elif root.right:
                travel(root.right, 1)

        travel(root, 1)
        
        return result