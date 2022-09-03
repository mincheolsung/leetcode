class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        result = []
        def backtrack(temp: List, i: int):
            if len(temp) == n:
                result.append(int("".join(temp[:])))
                temp = []
                return

            for digit in range(10):
                if i > 0 and abs(digit - int(temp[i-1])) != k: 
                    continue
                if i == 0 and digit == 0:
                    continue
                temp.append(str(digit))
                backtrack(temp, i+1)
                temp.pop()
        
        backtrack([],0)
        
        
        return result
                    
                    
                
        
            