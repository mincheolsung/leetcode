# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root: Optional[TreeNode])->int:
            nonlocal globalMax

            if not root:
                return 0            

            leftMax = helper(root.left)
            rightMax = helper(root.right)

            localMax = max([root.val, root.val + leftMax, root.val + rightMax])
            globalMax = max([globalMax, localMax, root.val + leftMax + rightMax])

            return localMax

        globalMax = float('-inf')
        helper(root)
        return globalMax            

            

