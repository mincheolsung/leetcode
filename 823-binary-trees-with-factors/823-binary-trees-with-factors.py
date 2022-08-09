class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        
        dp = {}

        arr.sort();
    
        mySet = set(arr);
        
        for num in arr:
            dp[num] = 1
        
        for i in range(0, len(arr)):
            for j in range(i-1, -1, -1):
                p = arr[i]
                x = arr[j]
                y = arr[i]/arr[j]
                
                if p == x*y and y in mySet:
                    dp[p] = (dp[p] + dp[x]*dp[y])%mod
        
        return (sum(dp.values()))%mod
        