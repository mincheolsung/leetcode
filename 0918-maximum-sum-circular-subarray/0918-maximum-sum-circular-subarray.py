class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        curMax = 0
        curMin = 0
        maxSoFar = nums[0]
        minSoFar = nums[0]
        
        for i in range(len(nums)):
            total += nums[i]            
            curMax = max(curMax + nums[i], nums[i])
            curMin = min(curMin + nums[i], nums[i])
            maxSoFar = max(maxSoFar, curMax)
            minSoFar = min(minSoFar, curMin)

        return max(total-minSoFar, maxSoFar) if maxSoFar > 0 else maxSoFar