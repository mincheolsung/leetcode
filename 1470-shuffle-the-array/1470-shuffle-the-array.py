class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i,j = 0,n    
        res = []
        for i in range(n):
            j = i + n
            res.append(nums[i])
            res.append(nums[j])
        return res