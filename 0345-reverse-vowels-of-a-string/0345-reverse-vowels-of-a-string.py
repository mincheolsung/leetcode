class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(s: str)->bool:
            if s.lower() in "aeiouAEIOU":
                return True
            else:
                return False
        
        left = 0
        right = len(s)-1
        
        s = list(s)
        while left < right:
            while not isVowel(s[left]) and left < right:
                left += 1
                
            while not isVowel(s[right]) and left < right:
                right -= 1
                
            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1

        return "".join(s)