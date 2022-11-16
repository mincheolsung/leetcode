class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = 0
        
        for num in nums:
            if freq & (1<<num):
                return num
            freq |= (1 << num)
        
        