class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r == m:
                return c
            if grid[r][c] == 1:
                if c == n-1 or grid[r][c+1] == -1:
                    return -1
            else:
                if c == 0 or grid[r][c-1] == 1:  
                    return -1

            return dfs(r + 1, c + grid[r][c])

        result = []
        for c in range(n):
            result.append(dfs(0,c))
        return result