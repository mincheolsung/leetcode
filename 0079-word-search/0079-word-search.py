class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r:int, c:int, temp: str) -> bool:                     
            if len(temp) == 1 and board[r][c] == temp[0]:
                return True

            if board[r][c] != temp[0]:
                return False

            visited[r][c] = 1
            
            for moveR,moveC in [(1,0),(0,1),(-1,0),(0,-1)]:
                newR,newC = r + moveR, c + moveC
                if 0 <= newR < m and 0 <= newC < n and visited[newR][newC] == 0:
                    if dfs(newR, newC, temp[1:]):
                        return True

            visited[r][c] = 0

            return False

        m = len(board)
        n = len(board[0])
        visited = [[0]*n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if dfs(r,c,word):
                    return True
        return False