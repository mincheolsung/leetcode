class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        counter = Counter()
        
        for i in range(n):
            if len(counter) > k:
                counter[nums[i-k-1]] -= 1

            counter[nums[i]]+=1
            
            if counter[nums[i]] > 1:
                return True

        return False
        
        
    
        