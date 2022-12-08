# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:        
        def dfs(root: Optional[TreeNode], traversal: List[int]):
            stack = [root]
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    traversal.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        traversal1 = []
        traversal2 = []
        dfs(root1, traversal1)
        dfs(root2, traversal2)
        return traversal1 == traversal2
            