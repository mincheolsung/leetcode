class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        visited = [[0]*n for _ in range(m)]
        q = [(0, entrance[0], entrance[1])]
        cnt = 0

        while q:
            d,x,y = heapq.heappop(q)
            if (x != entrance[0] or y != entrance[1]) and (x == 0 or x == m-1 or y == 0 or y == n-1):
                return d

            for moveX,moveY in [(0,1),(1,0),(-1,0),(0,-1)]:
                newX = x + moveX
                newY = y + moveY
                if 0 <= newX < m and 0 <= newY < n and maze[newX][newY] == '.' and visited[newX][newY] == 0:
                    visited[newX][newY] = 1
                    heapq.heappush(q, (d+1, newX, newY))

        return -1