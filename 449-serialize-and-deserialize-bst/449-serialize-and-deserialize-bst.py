# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        
        def pre_order(root):
            if root:
                result.append(root.val)
                pre_order(root.left)
                pre_order(root.right)
        
        pre_order(root)
        return ' '.join(str(val) for val in result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())
        
        def bst(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                root = TreeNode(val)
                root.left = bst(minVal, val)
                root.right = bst(val, maxVal)
                return root

        return bst(float('-infinity'), float('infinity'))            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans