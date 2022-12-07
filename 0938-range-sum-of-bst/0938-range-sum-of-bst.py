# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        
        ans = 0
        while stack:
            node = stack.pop()
            if not node:
                return ans
            
            if low <= node.val <= high:
                ans += node.val

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return ans