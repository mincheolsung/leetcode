class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        n = len(pressedKeys)
        dp = {}

        i = 0
        dp[(i,1)] = 1
        dp[(i,2)] = 2
        dp[(i,3)] = 4
        for j in range(4,n+1):
            dp[(i,j)] = (dp[(i,j-1)] + dp[(i,j-2)] + dp[(i,j-3)])%1000000007

        i = 1
        dp[(i,1)] = 1
        dp[(i,2)] = 2
        dp[(i,3)] = 4
        dp[(i,4)] = 8
        for j in range(5,n+1):
            dp[(i,j)] = (dp[(i,j-1)] + dp[(i,j-2)] + dp[(i,j-3)] + dp[(i,j-4)])%1000000007

        result = 1
        cur = 0
        while cur < n-1:
            repeated = 1
            while cur < n-1 and pressedKeys[cur] == pressedKeys[cur+1]:
                repeated += 1
                cur+=1
            num = int(pressedKeys[cur])
            if num in [7,9]:
                num = 1
            else:
                num = 0
            result = (result*dp[(num,repeated)])%1000000007
            cur+=1

        return result