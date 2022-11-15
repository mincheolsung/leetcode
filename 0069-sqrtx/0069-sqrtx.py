class Solution:
    def mySqrt(self, x: int) -> int:
        for num in range(2**16):
            if num*num > x:
                return num-1
            
        