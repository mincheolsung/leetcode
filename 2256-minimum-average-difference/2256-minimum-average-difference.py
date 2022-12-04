class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        presum = [0]*(n+1)
        
        for i in range(n):
            presum[i+1] = nums[i]+presum[i]
        
        average = [0]*n
        
        for i in range(n-1):
            average[i] = abs(presum[i+1]//(i+1) - (presum[n]-presum[i+1])//(n-i-1))

        average[n-1] = presum[n]//n
            
        return average.index(min(average))
        