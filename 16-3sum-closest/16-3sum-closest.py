class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()

        minDiff = float('inf')
        result = 0
        
        for i in range(n-2):
            if i > 1 and nums[i] == nums[i-1]:
                continue
            
            left = i+1
            right = n-1
            diff = 0
            while left < right:
                #while left+1 < right and left-1 >= 0 and nums[left] == nums[left-1]:
                #    left+=1
                    
                #while left < right-1 and right+1 < n and nums[right] == nums[right+1]:
                #    right-=1
                
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
            