class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        string = list(s)        
        n = len(string)
        if n%2 == 1:
            return False

        i = 0
        while i < n:
            close = string[i]
            if close in "({[":
                stack.append(close)
            else:
                if not stack:
                    return False
                open = stack.pop()
                if open == "(" and close != ")":
                    return False
                elif open == "{" and close != "}":
                    return False
                elif open == "[" and close != "]":
                    return False
            i+=1
    
        if stack:
            return False
    
        return True
        