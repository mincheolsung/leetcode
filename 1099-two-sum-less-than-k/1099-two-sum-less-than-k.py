class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        
        ans = -1
        while left < right:
            if nums[left] + nums[right] >= k:
                right-=1
            else:
                ans = max(ans, nums[left]+nums[right])
                left+=1

        return ans
            