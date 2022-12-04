class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mySet = {}
        
        for i in range(n):
            if target - nums[i] in mySet:
                return sorted([mySet[target - nums[i]], i])
        
            mySet[nums[i]] = i
                
        
        