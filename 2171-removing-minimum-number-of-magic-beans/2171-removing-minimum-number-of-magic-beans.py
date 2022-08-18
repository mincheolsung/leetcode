class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        beans.sort()
        
        result = sys.maxint
        total = sum(beans)
        
        for i in range(len(beans)):
            remaining = beans[i]*(len(beans)-i)
            removed = total - remaining
            result = min(result, removed)
    
        return result