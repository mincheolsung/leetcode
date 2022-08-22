class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n > 0:
            temp = log(n,4)
            return (temp == int(temp))
        
        return False
        
        