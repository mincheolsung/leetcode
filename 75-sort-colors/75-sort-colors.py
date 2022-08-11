class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # red, white, blue
        # red red red white white white blue blue blue
            
        r = 0;
        b = len(nums)-1;
        
        i = 0
        while (i < len(nums)):
            if nums[i] == 0 and i > r:
                nums[i], nums[r] = nums[r], nums[i]
                r+=1;
            elif nums[i] == 2 and i < b:
                nums[i], nums[b] = nums[b], nums[i]
                b-=1
            else:
                i+=1