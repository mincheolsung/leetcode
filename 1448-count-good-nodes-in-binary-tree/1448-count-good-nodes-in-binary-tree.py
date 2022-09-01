# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        result = 0
        
        def dfs(root: TreeNode, maxVal: int):
            nonlocal result
            
            if not root:
                return
            
            curMax = maxVal
            if root.val >= maxVal:
                result += 1
                curMax = root.val
                
            dfs(root.left, curMax)
            dfs(root.right, curMax)
            
        
        dfs(root, float('-inf'))
        
        return result
            
            
                