class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(temp:list):
            nonlocal n
            if len(temp) == n:
                result.append(temp[:])
                return
                
            for num in nums:
                if num not in temp:
                    temp.append(num)
                    backtrack(temp)
                    temp.pop()

        n = len(nums)
        result = []
        backtrack([])
        return result