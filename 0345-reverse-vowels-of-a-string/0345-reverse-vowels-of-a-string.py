class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(s: str)->bool:
            s = s.lower()
            if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
                return True
            else:
                return False
        
        left = 0
        right = len(s)-1
        
        s = list(s)
        while left < right:
            while isVowel(s[left]) == False and left < right:
                left += 1
                
            while isVowel(s[right]) == False and left < right:
                right -= 1
                
            s[left],s[right] = s[right],s[left]

            left += 1
            right -= 1

        return "".join(s)