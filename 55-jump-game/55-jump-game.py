class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        dp = [0]*len(nums)
        dp[0] = 1
        
        for i in range(len(nums)):
            if dp[i] == 1:
                for j in range(i+nums[i], i-1, -1):
                    if j < len(nums):
                        dp[j] = 1
                        if dp[-1] == 1:
                            return True

        return dp[-1] == 1
        