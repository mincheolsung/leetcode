class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(queries)
        sum = 0
        for num in nums:
            if num % 2 == 0:
                sum+=num
        
        result = []
        
        for i in range(n):        
            val, index = queries[i]
            
            old = nums[index] 
            new = old + val
            
            if old % 2 == 0 and new % 2 == 0:
                sum += val
            elif old % 2 == 0 and new % 2 == 1:
                sum -= nums[index]
            elif old % 2 == 1 and new % 2 == 0:
                sum += (nums[index]+val)
    
            nums[index] = new
            result.append(sum)
    
        return result
        
        
        
        