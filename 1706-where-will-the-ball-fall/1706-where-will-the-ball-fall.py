class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r == m:
                return c
            if c == -1 or c == n:
                return -1

            if grid[r][c] == 1:
                if c == n-1 or grid[r][c+1] == -1:
                    return -1
            else:
                if c == 0 or grid[r][c-1] == 1:  
                    return -1
            
            return dfs(r + 1, c + grid[r][c])

        result = []
        for c in range(n):
            loc = dfs(0,c)
            if loc == -1:
                result.append(-1)
            else:
                result.append(loc)

        return result