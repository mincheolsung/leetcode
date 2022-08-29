void dfs(char **grid, int gridSize, int gridColSize, int i, int j) {
    if (i == -1 || j == -1) {
        return;
    }
    
    if (i > gridSize - 1 || j > gridColSize - 1) {
        return;
    }
    
    if (grid[i][j] == '0') {
        return;
    }

    grid[i][j] = '0';
    dfs(grid, gridSize, gridColSize, i-1, j);
    dfs(grid, gridSize, gridColSize, i, j-1);
    dfs(grid, gridSize, gridColSize, i+1, j);
    dfs(grid, gridSize, gridColSize, i, j+1);
}

int numIslands(char** grid, int gridSize, int* gridColSize){
    int i,j;
    int result = 0;
    
    for (i = 0; i < gridSize; i++) {
        for (j = 0; j < gridColSize[i]; j++) {
            if (grid[i][j] == '1') {
                dfs(grid, gridSize, gridColSize[i], i, j);
                result++;
            }            
        }
    }
    
    return result;
}