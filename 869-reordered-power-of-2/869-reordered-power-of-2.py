class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))

        target = 1        
        while target < 1000000000:
            target_cnt = Counter(str(target))
            if target_cnt == cnt:
                return True
            
            target <<= 1
        
        return False