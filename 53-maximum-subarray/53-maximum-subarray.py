class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentSum = 0
        result = 0
        
        for num in nums:
            currentSum += num
            
            if currentSum <= 0:
                currentSum = 0
            
            result = max(result, currentSum)
                
        return result if result != 0 else max(nums)