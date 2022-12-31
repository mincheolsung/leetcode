class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(x: int, y: int, path: List[tuple]):
            nonlocal ans
            nonlocal numSquare
            nonlocal m
            nonlocal n
            
            if grid[x][y] == 2 and len(path) == numSquare:
                ans+=1
                return
            
            for moveX,moveY in [(1,0),(0,1),(-1,0),(0,-1)]:
                nextX = x + moveX
                nextY = y + moveY
                if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][nextY] != -1 and (nextX,nextY) not in path:
                    dfs(nextX, nextY, path + [(nextX, nextY)])
            
        m = len(grid)
        n = len(grid[0])
        ans = 0
        numSquare = 2
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    numSquare+=1
                elif grid[x][y] == 1:
                    start = (x,y)
        print(numSquare)
        dfs(start[0], start[1], [(start[0],start[1])])

        return ans
            
            
            
            
                              