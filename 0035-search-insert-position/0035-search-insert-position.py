class Solution:
    # bisect_left
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right-left)//2
    
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid
        
        return left
    
    def bisect_right(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right-left)//2
    
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid
        
        return left