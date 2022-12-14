class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)
        
        dp = [0]*n
        
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(n-2):
            dp[i+2] = max(nums[i+2] + dp[i], dp[i+1])
            
        return dp[n-1]
        
        
        