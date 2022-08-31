class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])
        q = [(0, "", ball[0], ball[1])]
        stopped = {(ball[0], ball[1]): [0, ""]}

        while q:
            dist,pattern,x,y = heapq.heappop(q)
            if [x,y] == hole:
                return pattern
            
            for moveX,moveY,p in ((0,1,"r"),(0,-1,"l"),(1,0,"d"),(-1,0,"u")):
                newX, newY = x, y
                d = 0
                while 0 <= newX+moveX <= m-1 and 0 <= newY+moveY <= n-1 and maze[newX+moveX][newY+moveY] != 1:
                    newX += moveX
                    newY += moveY
                    d += 1
                    if [newX,newY] == hole:
                        break

                if (newX, newY) not in stopped or [dist + d, pattern + p] < stopped[(newX,newY)]:
                    stopped[(newX, newY)] = [dist + d, pattern + p]
                    heapq.heappush(q, (dist + d, pattern + p, newX, newY))

        return "impossible"