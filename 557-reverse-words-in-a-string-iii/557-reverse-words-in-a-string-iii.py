class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        
        for word in s[::-1].split()[::-1]:
            result += word + " "
            
        return result[:-1]