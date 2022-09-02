class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[2]

        for i in range(n-2):
            left = i+1
            right = n-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum == target:
                    return sum
                
                if abs(target - sum) < abs(result - target):
                    result = sum

                if sum < target:
                    left+=1
                elif sum > target:
                    right-=1
    
        return result
            