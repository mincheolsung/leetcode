class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        runningSum = 0
        seen = {0:-1}

        for i in range(n):
            runningSum += nums[i]
            if k != 0:
                runningSum %= k
            prev = seen.get(runningSum)
            if prev != None:
                if i - prev > 1:
                    return True
            else:
                seen[runningSum] = i

        return False
                
            