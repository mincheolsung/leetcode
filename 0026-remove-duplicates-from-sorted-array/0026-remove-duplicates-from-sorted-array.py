class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0
        i = 0
        while index < n and i < n:
            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            
            nums[index] = nums[i]
            index+=1
            i+=1

        return index