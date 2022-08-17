# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = []

        def level_order(root, level):
            if not root:
                return

            if len(result) == level:
                result.append(deque())
            
            if level % 2 == 0:
                result[level].append(root.val)
                level_order(root.left, level+1)
                level_order(root.right, level+1)
            else:
                result[level].appendleft(root.val)
                level_order(root.left, level+1)
                level_order(root.right, level+1)

        level_order(root, 0)
        
        return result