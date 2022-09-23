class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s: str)->bool:
            cnt = 0
            for c in s:
                if cnt < 0:
                    return False

                if c == "(":
                    cnt+=1
                else:
                    cnt-=1
                
            if cnt != 0:
                return False
            else:
                return True
                        
        def backtrack(n: int, s: str):
            if n == 0:
                if isValid(s):
                    result.add(s)
                    return
            
            for i in range(len(s)+1):
                temp = s[:i] + "(" + s[i:] + ")"
                if temp not in result:
                    backtrack(n-1, temp)
        
        result = set()
        backtrack(n, "")
        return list(result)