class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        index = 0
        cur = 0
        result = ""
        minimum = 200

        for s in strs:
            minimum = min(minimum, len(s))
        
        
        
        while index < minimum:
            target = strs[0][index]
            
            for i in range(1, len(strs)):
                if target != strs[i][index]:
                    return result
    
            result += target
                
            index += 1
            
        return result