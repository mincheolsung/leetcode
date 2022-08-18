# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        traversal = []
        length = 1
        global len_left
        len_left = 101
        global len_right
        len_right = -101
        
        def length_measure(root, col):
            if not root:
                return
            
            global len_left
            global len_right

            len_left = min(len_left, col)
            len_right = max(len_right, col)
            
            length_measure(root.left, col-1)
            length_measure(root.right, col+1)
            
        length_measure(root,0)

        len_left = 0 - len_left
        length += (len_left + len_right)
        
        for _ in range(length):
            traversal.append([])
        
        q = collections.deque()
        q.append([root, len_left])
        
        while q:
            node = q.popleft()
            p = node[0]
            col = node[1]
            traversal[col].append(p.val)
            
            if p.left:
                q.append([p.left, col-1])
            
            if p.right:
                q.append([p.right, col+1])
                
        return traversal
        
            
            