void backtrack(int **grid, int gridSize, int *gridColSize, int i, int j, int *cnt) {
    if (i == -1 || j == -1 || i == gridSize || j == gridColSize[0]) {
        return;
    }

    if (grid[i][j] == -1) {
        return;
    }
    
    if (grid[i][j] == 2) {
        for (int ii = 0; ii < gridSize; ii++) {
            for (int jj = 0; jj < gridColSize[0]; jj++) {
                if (grid[ii][jj] == 0) {
                    return;
                }       
            }
        }
        (*cnt)++;
        return;
    }

    grid[i][j] = -1;

    backtrack(grid, gridSize, gridColSize, i-1, j, cnt);
    backtrack(grid, gridSize, gridColSize, i, j-1, cnt);
    backtrack(grid, gridSize, gridColSize, i+1, j, cnt);
    backtrack(grid, gridSize, gridColSize, i, j+1, cnt);
    
    grid[i][j] = 0;
}

int uniquePathsIII(int** grid, int gridSize, int* gridColSize){
    int result = 0;
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridColSize[0]; j++) {
            if (grid[i][j] == 1) {
                backtrack(grid, gridSize, gridColSize, i, j, &result);
                return result;
            }       
        }
    }
    
    return result;
}