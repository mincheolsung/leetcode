class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]*(n+1)
        
        for i in range(n):
            presum[i+1] = nums[i]+presum[i]
        
        minAverage = float('inf')
        ans = 0

        for i in range(n-1):
            temp = abs(presum[i+1]//(i+1) - (presum[n]-presum[i+1])//(n-i-1))
            if temp < minAverage:
                minAverage = temp
                ans = i
        
        if presum[n]//n < minAverage:
            return n-1
        else:
            return ans
