class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index = stack[-1][0]
                ans[index] = i-index
                stack.pop()
            stack.append((i,temp))
        return ans 