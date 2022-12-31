# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [r,c] = binaryMatrix.dimensions()
                
        def findOne(r:int, c:int)->int:
            left = 0
            right = c

            while left < right:
                mid = left + (right - left)//2
            
                if binaryMatrix.get(r,mid) == 0:
                    left = mid+1
                else:
                    right = mid
        
            return left
        
        ans = float('inf')
        for i in range(r):
            ans = min(ans, findOne(i,c))
            
        return ans if ans < c else -1