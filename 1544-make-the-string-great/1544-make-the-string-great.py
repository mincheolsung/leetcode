class Solution:
    def makeGood(self, s: str) -> str: 
        if len(s) < 2:
            return s

        for i in range(len(s)-1):
            if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                print(s[:i]+s[i+2:])
                return self.makeGood(s[:i]+s[i+2:])

        return s 