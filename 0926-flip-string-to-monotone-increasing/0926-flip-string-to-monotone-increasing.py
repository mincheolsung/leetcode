class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        zero = [0]*n
        one = [0]*n
        cnt1 = 0
        cnt2 = 0
        
        for i in range(n):
            if s[i] == "1":
                cnt1 += 1
            if s[n-1-i] == "0":
                cnt2 += 1  
            one[i] = cnt1
            zero[n-1-i] = cnt2

        ans = float('inf')
        for i in range(n):
            ans = min(ans, zero[i]+one[i]-1)
            
        return ans