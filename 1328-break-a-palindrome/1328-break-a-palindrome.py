class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        
        i = 0
        while i < n//2 and palindrome[i] == 'a':
            i+=1
        
        result = list(palindrome)
        if i == n//2:
            result[n-1] = 'b'
        else:
            result[i] = 'a'

        return ''.join(result)
            
            
            
            
        