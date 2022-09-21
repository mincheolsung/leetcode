class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def isEven(num: int)-> bool:
            return (num%2 == 0)

        n = len(queries)
        sum = 0
        for num in nums:
            if isEven(num):
                sum+=num
        
        result = []
        
        even = [True,True]
        for i in range(n):        
            val, index = queries[i]
            
            even[0] = isEven(nums[index])
            even[1] = isEven(nums[index]+val)
            
            if even[0] and even[1]:
                sum += val
            elif even[0] and not even[1]:
                sum -= nums[index]
            elif not even[0] and even[1]:
                sum += (nums[index]+val)
                
            nums[index] += val
            result.append(sum)
    
        return result
        
        
        
        