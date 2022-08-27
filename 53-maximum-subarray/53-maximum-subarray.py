class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currentSum = 0
        result = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum <= 0:
                currentSum = 0
            
            result = max(result, currentSum)
             
        if result != 0:
            return result
        else:
            return max(nums)