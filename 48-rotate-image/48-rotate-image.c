void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    int temp, tmp;
    int r,c;
    int i,j;
    
    int **visited;
    visited = calloc(matrixSize, sizeof(int *));
    if (visited == NULL) {
        return;
    }
    
    for (i = 0; i < matrixSize; i++) {
        visited[i] = calloc(matrixColSize[0], sizeof(int));
        if (visited[i] == NULL) {
            return;
        }
    }

    for (i = 0; i < matrixSize/2; i++) {
        for (j = 0; j < matrixColSize[i]-i; j++) {
            r = i;
            c = j;

            temp = matrix[r][c];
            while (visited[r][c] == 0) {
                swap(&matrix[c][matrixColSize[0]-1-r], &temp);
                visited[r][c] = 1;

                tmp = c;
                c = matrixColSize[0]-1-r;
                r = tmp;
            }
        }   
    }
}