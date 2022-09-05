"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        travel = []
        def helper(root: 'Node', level: int):
            if not root:
                return
            
            if len(travel) == level:
                travel.append([])
                
            travel[level].append(root.val)
            
            for child in root.children:
                helper(child, level+1)

        helper(root, 0)
        
        return travel