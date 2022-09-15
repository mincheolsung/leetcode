class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        answer = 0
        n = len(s)

        if n <= 2:
            return n

        dp = [0]*n
        for i in range(n-1):
            dp[i] = 1
            visited = defaultdict(int)
            visited[s[i]] = 1
            length = 1
            for j in range(i+1, n):
                if visited[s[j]] == 0:
                    dp[j] = dp[j-1] + 1
                    visited[s[j]] += 1
                else:
                    dp[j] = dp[j-1]
            
                if dp[j] <= 2:  
                    length += 1
                else:
                    break

            answer = max(answer, length)
            
        return answer