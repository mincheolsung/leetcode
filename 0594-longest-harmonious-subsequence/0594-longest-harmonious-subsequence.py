class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        
        for key in cnt.keys():
            if key+1 in cnt:
                ans = max(ans, cnt[key] + cnt[key+1])
        return ans
