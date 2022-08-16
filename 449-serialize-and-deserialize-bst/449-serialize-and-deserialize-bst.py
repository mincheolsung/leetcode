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
        vals = [int(val) for val in data.split()]
        
        def bst(vals):
            if not vals:
                return None

            val = vals[0]
            node = TreeNode(val)
            
            i = 1
            while i < len(vals) and vals[i] < val:
                i+=1
                
            node.left = bst(vals[1:i])
            node.right = bst(vals[i:])
            
            return node
            
        return bst(vals)            
        

        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans