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
        
        if not preorder:
            return None
        
        node = TreeNode(preorder[0])
        index = 1
        
        while index < len(preorder) and preorder[index] < node.val:
            index+=1
        
        node.left = self.bstFromPreorder(preorder[1:index])
        node.right = self.bstFromPreorder(preorder[index:])
        
        return node

                