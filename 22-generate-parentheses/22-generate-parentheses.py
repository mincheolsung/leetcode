class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open: int, close: int):
            if open == close == n:
                result.append("".join(temp))
            
            if open < n:
                temp.append("(")
                backtrack(open+1, close)
                temp.pop()
                
            if close < open:
                temp.append(")")
                backtrack(open, close+1)
                temp.pop()
    
        temp = []
        result = []
        backtrack(0,0)
        return result