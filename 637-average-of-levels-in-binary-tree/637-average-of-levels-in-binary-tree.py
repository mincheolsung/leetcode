# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        travel = []
        
        def levelOrder(root: Optional[TreeNode], level: int):
            if not root:
                return
            
            if len(travel) == level:
                travel.append([])
                
            travel[level].append(root.val)
            
            levelOrder(root.left, level+1)
            levelOrder(root.right, level+1)
            
        levelOrder(root, 0)
        
        for val in travel:
            result.append(sum(val)/len(val))
            
        return result