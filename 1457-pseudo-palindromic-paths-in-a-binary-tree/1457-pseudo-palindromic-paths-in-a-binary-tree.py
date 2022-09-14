# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:        
        def dfs(root: Optional[TreeNode], path: int):
            path ^= (1 << root.val)
            if not root.left and not root.right:
                if path & (path-1) == 0:
                    answer[0]+=1
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)

        answer = [0]
        dfs(root, 0)
        return answer[0]