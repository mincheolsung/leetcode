# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        result = []
        
        def helper(root, index):
            if not root:
                return False
            
            if len(result) == index:
                result.append([])
            
            if not root.left and not root.right:
                result[index].append(root.val)
                return True
            
            if helper(root.left, index):
                root.left = None
                
            if helper(root.right, index):
                root.right = None
            
            return False
        
        index = 0
        while True:
            if helper(root, index):
                return result
            print(result)
            index+=1
            