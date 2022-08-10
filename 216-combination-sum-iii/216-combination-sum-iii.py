class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        
        result = []
        comb = []
        
        def backtrack(start, target):
            if len(comb) == k and target == 0:
                result.append(list(comb))
                return
            
            for num in range(start,10):
                if target - num >= 0:
                    comb.append(num)
                    backtrack(num+1, target-num)
                    comb.pop()
    
        backtrack(1, n)
        return result
                    
            