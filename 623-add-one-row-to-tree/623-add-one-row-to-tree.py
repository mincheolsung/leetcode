# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        if depth == 2:
            temp = root.left
            root.left = TreeNode(val)
            root.left.left = temp
            temp = root.right
            root.right = TreeNode(val)
            root.right.right = temp
            return root 

        if root.left:
            root.left = self.addOneRow(root.left, val, depth-1)
        if root.right:
            root.right = self.addOneRow(root.right, val, depth-1)

        return root