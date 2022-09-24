# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.left and not root.right and root.val == targetSum:
            return [[root.val]]

        res = []
        
        if root.left:
            for item in self.pathSum(root.left, targetSum - root.val):
                item = [root.val] + item
                res.append(item)

        if root.right:
            for item in self.pathSum(root.right, targetSum - root.val):
                item = [root.val] + item
                res.append(item)

        return res