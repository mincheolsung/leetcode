class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        result = 0
        prev = 0
        
        for c in s:
            result += roman[c] if prev >= roman[c] or prev == 0 else roman[c] - prev - prev
            prev = roman[c]

        return result
            
                