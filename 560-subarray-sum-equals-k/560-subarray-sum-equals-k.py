class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currentSum = 0
        
        count = Counter()
        count[0] = 1
        
        for num in nums:
            currentSum += num
            result += count[currentSum - k]
            count[currentSum] += 1
            
        return result
        