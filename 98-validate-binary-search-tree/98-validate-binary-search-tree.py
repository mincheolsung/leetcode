# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        inorder = []
        
        def traversal(root):
            if root is None:
                return
            
            traversal(root.left)
            inorder.append(root.val)
            traversal(root.right)
            
        traversal(root)
        
        for i in range(0,len(inorder)-1):
            if inorder[i] >= inorder[i+1]:
                return False
            
        return True

        