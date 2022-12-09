# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], vals: List[int]):
            nonlocal ans
            vals.append(root.val)

            ans = max(ans, max(vals)-min(vals))
            
            if root.left:
                dfs(root.left, vals)
    
            if root.right:
                dfs(root.right, vals)
            
            vals.pop()                     

        ans = float('-inf')
        
        dfs(root, [])

        return ans