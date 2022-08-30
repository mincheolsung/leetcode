class Solution:
    '''
    # BFS
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n, visited = len(maze), len(maze[0]), set()
        q = deque([(start[0],start[1])])
        
        while q:
            x,y = q.popleft()
            
            if (x,y) in visited:
                continue
            visited.add((x,y))
            
            if [x,y] == destination:
                return True
            
            for moveX, moveY in ((1,0),(0,1),(-1,0),(0,-1)):
                newX, newY = x,y
                while 0 <= newX+moveX <= m-1 and 0 <= newY+moveY <= n-1 and maze[newX+moveX][newY+moveY] == 0:
                    newX += moveX
                    newY += moveY
                
                q.append((newX,newY))

        return False
     '''
        
    # DFS
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = set()
        
        def dfs(x: int, y: int)-> bool:
            if (x,y) in visited:
                return False
            visited.add((x,y))

            if [x,y] == destination:
                return True
    
            m = len(maze)
            n = len(maze[0])
            
            for (moveX, moveY) in [(0,1),(1,0),(0,-1),(-1,0)]:
                newX,newY = x,y
                while 0 <= newX + moveX <= m-1 and 0 <= newY + moveY <= n-1 and maze[newX + moveX][newY + moveY] == 0:
                    newX += moveX
                    newY += moveY
                    
                if dfs(newX,newY):
                    return True

            return False
                        
        return dfs(start[0], start[1])