class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        temp = []
        
        candidates.sort()
        
        def backtrack(index, candidates, target):            
            if target == 0:
                result.append(list(temp))
                return

            for i in range(index, len(candidates)):
                if target - candidates[i] >= 0:
                    temp.append(candidates[i])
                    backtrack(i, candidates, target-candidates[i])
                    temp.pop()

        backtrack(0, candidates, target)
        
        return result