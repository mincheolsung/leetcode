class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bisect_right
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right-left)//2
    
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        
        return left 