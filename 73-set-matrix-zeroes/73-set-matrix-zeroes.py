class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        visited = [[0]*len(matrix[0]) for _ in range(len(matrix))]
        
        def dfs(row: int, col: int, direction: int):
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                return

            if matrix[row][col] !=0:
                matrix[row][col] = -2**31-1
    
            match direction:
                case 0:
                    dfs(row+1,col, 0)
                case 1:
                    dfs(row,col+1, 1)
                case 2:
                    dfs(row-1,col, 2)
                case 3:
                    dfs(row,col-1, 3)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    dfs(r,c, 0)
                    dfs(r,c, 1)
                    dfs(r,c, 2)
                    dfs(r,c, 3)
                    

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == -2**31-1:
                    matrix[r][c] = 0
            
                
            