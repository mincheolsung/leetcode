# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], curMax: int, curMin: int):
            curMax = max(curMax, root.val)
            curMin = min(curMin, root.val)
            ans[0] = max(ans[0], abs(curMax - curMin))

            if root.left:
                dfs(root.left, curMax, curMin)
            if root.right:
                dfs(root.right, curMax, curMin)

        ans = [0]
        dfs(root, root.val, root.val)
        return ans[0]