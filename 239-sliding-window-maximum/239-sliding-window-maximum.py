class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        
        def clean(i: int):
            if q and q[0] == i-k:
                q.popleft()

            while q and nums[i] > nums[q[-1]]:
                q.pop()

        q = deque()
        currentMax = nums[0]
        currentMaxIndex = 0
        for i in range(k):
            clean(i)
            q.append(i)
            if currentMax < nums[i]:
                currentMax = nums[i]
                currentMaxIndex = i

        result.append(currentMax)
        for i in range(k, n):
            clean(i)
            q.append(i)
            result.append(nums[q[0]])

        return result
                