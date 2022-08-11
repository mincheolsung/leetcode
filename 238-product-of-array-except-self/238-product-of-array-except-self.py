class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [1]*len(nums)
        
        for i in range(1, len(nums)):
            result[i] = nums[i-1] * result[i-1]
            
        temp = 1
        for i in range(len(nums)-2, -1, -1):
            temp = nums[i+1] * temp
            result[i] *= temp
            
        return result