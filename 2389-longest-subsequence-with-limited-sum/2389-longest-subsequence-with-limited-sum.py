class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n,m = len(nums),len(queries)
        sortedNums = sorted(nums, reverse=True)
        totalSum = sum(nums)
        answer = [n]*m

        for i in range(m):
            temp = totalSum 
            for j in range(n):
                if temp <= queries[i]:
                    break
                temp -= sortedNums[j]
                answer[i] -= 1

        return answer