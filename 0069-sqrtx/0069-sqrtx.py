class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = 2**16
        
        while left < right:
            pivot = left + (right - left)//2
            
            if pivot*pivot <= x:
                left = pivot + 1
            else:
                right = pivot
    
        return left-1
            
        