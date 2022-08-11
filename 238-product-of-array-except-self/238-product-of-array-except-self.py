class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        temp1 = [1]*len(nums)
        temp2 = [1]*len(nums)
        
        for i in range(1, len(nums)):
            temp1[i] = nums[i-1] * temp1[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            temp2[i] = nums[i+1] * temp2[i+1]
            
        for i in range(len(nums)):
            temp1[i] *= temp2[i]
            
            
        return temp1