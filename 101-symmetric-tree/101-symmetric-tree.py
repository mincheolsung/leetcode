# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def postOrder1(root, traversal):
            if root is None:
                traversal.append(-101)
                return
            
            postOrder1(root.left, traversal)
            postOrder1(root.right, traversal)
            traversal.append(root.val)

            
        def postOrder2(root, traversal):
            if root is None:
                traversal.append(-101)
                return
            
            postOrder2(root.right, traversal)
            postOrder2(root.left, traversal)
            traversal.append(root.val)

        traversal1 = []
        traversal2 = []
        
        postOrder1(root.left,  traversal1)
        postOrder2(root.right, traversal2)

        if traversal1 == traversal2:
            return True
        else:
            return False