class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) is 0:
            return []
    
        dict = {}
        dict[2] = {'a','b','c'}
        dict[3] = {'d','e','f'}
        dict[4] = {'g','h','i'}
        dict[5] = {'j','k','l'}
        dict[6] = {'m','n','o'}
        dict[7] = {'p','q','r','s'}
        dict[8] = {'t','u','v'}
        dict[9] = {'w','x','y','z'}

        result = []
        
        def backtrack(index, temp):
            if index == len(digits):
                result.append(str(temp))
                return
            
            for digit in digits[index]:
                for s in dict[int(digit)]:
                    temp += s
                    backtrack(index+1, temp)
                    temp = temp[:-1]
            
        backtrack(0, "")
        
        return result
            