# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = defaultdict(list)
        result = []
    
        def helper(root: Optional[TreeNode], i: int, j: int):
            if not root:
                return
            
            if not dict[(i,j)]:
                dict[(i,j)] = [root.val]
            else:
                dict[(i,j)].append(root.val)
            
            helper(root.left, i-1, j+1)
            helper(root.right, i+1, j+1)
            
        helper(root, 0, 0)
        
        items = sorted(dict.items())
        (offset, _), _ = items[0]
        for (i,j),val in items:
            val.sort()
            if len(result) == i-offset:
                result.append(val)
            else:
                result[i-offset] += val
            
        return result
        
        
            
        
            
        
        