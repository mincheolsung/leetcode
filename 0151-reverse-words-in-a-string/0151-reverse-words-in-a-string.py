class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        i = 0
        while i < len(s):
            if i >= len(s):
                break
            if s[i] == '':
                s.remove(s[i])
            else:
                i+=1

        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1

        return " ".join(s)
        