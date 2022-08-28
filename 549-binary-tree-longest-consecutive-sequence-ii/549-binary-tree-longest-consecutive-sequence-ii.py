# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        global maxRes
        maxRes = 0
        
        def dfs(root: Optional[TreeNode]) -> [int, int]:
            global maxRes
            
            if not root:
                return [0,0]
            
            ascending = 1
            descending = 1

            if root.left:
                left = dfs(root.left)
                if root.left.val + 1 == root.val:
                    ascending = max(ascending, left[0] + 1)
                elif root.left.val - 1 == root.val:
                    descending = max(descending, left[1] + 1)
    
            if root.right:
                right = dfs(root.right)
                if root.right.val + 1 == root.val:
                    ascending = max(ascending, right[0] + 1)
                elif root.right.val -1 == root.val:
                    descending = max(descending, right[1] + 1)

            maxRes = max(maxRes, ascending + descending - 1)

            return [ascending, descending]
        
        dfs(root)
        return maxRes
            