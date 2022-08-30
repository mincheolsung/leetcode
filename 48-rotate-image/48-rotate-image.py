class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
    
        (0,1) <-- (2,0)
        (2,0) <-- (3,2)
        (3,2) <-- (1,3)
        (1,3) <-- (0,1)

        """

        n = len(matrix)
        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = temp