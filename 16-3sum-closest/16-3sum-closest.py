class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        
        result = float('inf')
        for i in range(n-2):
            left = i+1
            right = n-1
            
            while(left < right):
                tempSum = nums[i] + nums[left] + nums[right]

                if tempSum == target:
                    return tempSum

                if abs(tempSum-target) < abs(result-target):
                    result = tempSum

                if tempSum > target:
                    right-=1
                else:
                    left+=1
                    
        return result
                
            
            
            
        
            