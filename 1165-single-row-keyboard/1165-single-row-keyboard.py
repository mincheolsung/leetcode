class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        def findLen(char: str)->int:
            for i in range(len(keyboard)):
                if char == keyboard[i]:
                    return i;

        current = 0
        ans = 0
        for c in word:
            loc = findLen(c)
            ans += abs(loc-current)
            current = loc
        return ans