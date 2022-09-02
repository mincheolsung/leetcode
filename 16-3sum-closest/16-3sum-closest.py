class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        minDiff = float('inf')
        result = 0
        
        for i in range(n-2):
            left = i+1
            right = n-1
            diff = 0
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                diff = abs(target-s)

                if diff < minDiff:
                    result = s
                    minDiff = diff

                if s < target:
                    left+=1
                elif s > target:
                    right-=1
                else:
                    return s
    
        return result
            