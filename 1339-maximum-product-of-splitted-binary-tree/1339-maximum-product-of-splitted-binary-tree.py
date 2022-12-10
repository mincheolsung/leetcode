# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def getSum(root:Optional[TreeNode])->int:
            sum = root.val
            if root.left:
                sum += getSum(root.left)
            if root.right:
                sum += getSum(root.right)
            sums.append(sum)
            return sum

        ans = 0
        sums = []
        totalSum = getSum(root)
        
        for sum in sums:
            ans = max(ans, sum * (totalSum-sum))

        return int(ans%(1e9+7))