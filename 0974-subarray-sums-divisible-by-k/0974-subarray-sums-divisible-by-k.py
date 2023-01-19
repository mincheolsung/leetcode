class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        total = 0
        count = [0]*k
        count[0] = 1
        ans = 0
        for num in nums:
            total += num
            ans += count[total%k]
            count[total%k]+=1
        
        return ans