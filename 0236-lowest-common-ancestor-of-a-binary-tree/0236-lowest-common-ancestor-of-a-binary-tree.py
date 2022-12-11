# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root: 'TreeNode', target: 'TreeNode', path: List[int]):
            nonlocal found
            path.append(root)
            if root == target:
                paths.append(path[:])
                found = True
                return
            if not found and root.left:
                findPath(root.left, target, path)
            if not found and root.right:
                findPath(root.right, target, path)
            path.pop()

        paths = []
        found = False
        findPath(root, p, [])
        found = False
        findPath(root, q, [])
    
        for i in range(min(len(paths[0]), len(paths[1]))):
            if paths[0][i] == paths[1][i]:
                ans = paths[0][i]

        return ans