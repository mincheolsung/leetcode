# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        vals = collections.deque(preorder)
        
        def bst(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = bst(minVal, val)
                root.right = bst(val, maxVal)
                return root
        
        return bst(float("-infinity"), float("infinity"))