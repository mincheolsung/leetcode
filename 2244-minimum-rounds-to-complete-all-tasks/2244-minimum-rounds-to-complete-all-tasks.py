class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        ans = 0
        for key,val in cnt.items():
            while val >= 2:
                if val == 2:
                    val-=2
                    ans+=1
                elif val == 4:
                    val-=4
                    ans+=2
                else:
                    val-=3
                    ans+=1
            if val != 0:
                return -1
            
        return ans
                    
        