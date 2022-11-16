class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = 0
        for num in nums:
            target = 1 << num
            if freq & target:
                return num
            freq |= target