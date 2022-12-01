class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt1 = 0
        cnt2 = 0
        n = len(s)
        for i in range(n):
            if s[i] in 'aeiouAEIOU':
                if i < n//2:
                    cnt1+=1
                else:
                    cnt2+=1

        return cnt1 == cnt2