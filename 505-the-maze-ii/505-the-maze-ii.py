class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        stopped = {(start[0], start[1]):0}
        q = [(0, start[0], start[1])]
        
        while q:
            d, x, y = heappop(q)
              
            if [x, y] == destination:
                return d

            for moveX, moveY in ((1,0), (0,1), (-1,0), (0,-1)):
                newX, newY, move = x, y, 0
                while 0 <= newX + moveX <= m-1 and 0 <= newY + moveY <= n-1 and maze[newX+moveX][newY+moveY] == 0: 
                    newX += moveX
                    newY += moveY
                    move += 1
    
                if (newX, newY) not in stopped or (d + move) < stopped[(newX,newY)]:
                    stopped[(newX, newY)] = d + move
                    heappush(q, (d + move, newX, newY))
                    
        return -1