class Solution:
    def longestPalindrome(self, s: str) -> str:
        def lenPalindrome(s: str, i: int, j: int) -> str:
            while i > -1 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
                
            return s[i+1:j]
        
        result = ""
        for i in range(len(s)):
            temp = lenPalindrome(s,i,i+1)
            if len(temp) > len(result):
                result = temp[:]
            
            temp = lenPalindrome(s,i,i)
            if len(temp) > len(result):
                result = temp[:]
            
        return result
            
                
                
        