class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and log(n,2) % 2 == 0
        
        