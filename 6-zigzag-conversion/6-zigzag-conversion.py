class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        result = ['']*numRows
        
        index = 0
        step = 1
        
        for c in s:
            result[index]+=c
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index += step
            
        return ''.join(result)