class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s
        
        pattern = [["0" for i in range(len(s))] for i in range(numRows)]

        r = -1
        c = 0
        i = 0
        while i < len(s):
            r += 1
            pattern[r][c] = s[i];
            i += 1
            if r == numRows-1:
                while r > 0 and i < len(s):
                    r -= 1
                    c += 1
                    pattern[r][c] = s[i];
                    i += 1

        result = ""
        for i in range(0, numRows):
            for j in range(0, len(s)):
                if pattern[i][j] != "0":
                    result += pattern[i][j]
        
        return result