class Solution:
    def isPalindrome(self, s: str) -> bool:
        onlyAlphNum = ""
        for c in s.lower():
            if c in "0123456789abcdefghijklmnopqrstuvwxyz":
                onlyAlphNum+=c
        return onlyAlphNum[:] == onlyAlphNum[-1::-1]