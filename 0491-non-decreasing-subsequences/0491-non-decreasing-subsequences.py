class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        def backtrack(start:int, temp:List[int]):
            if len(temp) > 1:
                t = tuple(temp[:])
                if t not in visited:
                    ans.append(temp[:])
                    visited.add(t)

            for i in range(start, len(nums)):
                if not temp or (temp and temp[-1] <= nums[i]):
                    temp.append(nums[i])
                    backtrack(i+1, temp)
                    temp.pop()

        backtrack(0,[])
        return ans