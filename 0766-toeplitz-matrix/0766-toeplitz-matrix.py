class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def dfs(r: int, c: int, val: int)->bool:
            if r == m or c == n:
                return True
            if matrix[r][c] == val:
                return dfs(r+1, c+1, val)
            else:
                return False
        
        
        for r in range(m):
            if not dfs(r,0, matrix[r][0]):
                return False
            
        for c in range(1,n):
            if not dfs(0,c, matrix[0][c]):
                return False
            
        return True
            