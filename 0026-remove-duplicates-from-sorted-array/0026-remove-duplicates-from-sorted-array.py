class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        n = len(nums)

        while i < n and j < n:
            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            
            nums[j] = nums[i]
            i+=1
            j+=1
        
        return j
        