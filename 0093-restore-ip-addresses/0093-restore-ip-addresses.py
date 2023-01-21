class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(curStr: str, temp: List[str]):
            if len(temp) == 4 and not curStr:
                ans.append(".".join(temp))
                return
    
            for i in range(len(curStr)+1):
                integer = curStr[:i]
                if len(integer) > 1 and integer[0] == "0":
                    continue
                
                if len(integer) == 0:
                    continue
                
                if int(integer) > 255:
                    continue

                temp.append(integer)
                backtrack(curStr[i:], temp)
                temp.pop()
                
            
        backtrack(s,[])
        
        return ans