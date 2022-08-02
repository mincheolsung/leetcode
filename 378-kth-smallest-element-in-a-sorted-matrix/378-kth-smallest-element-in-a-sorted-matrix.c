int kthSmallest(int** matrix, int matrixSize, int* matrixColSize, int k) {
    int left,right,mid,cnt,i,j;
    
    left = matrix[0][0];
    right = matrix[matrixSize-1][matrixSize-1];

    while (left < right) {
        mid = left + (right-left)/2;
        cnt = 0;
        for (i = 0; i < matrixSize; i++) {
            for (j = 0; j < matrixSize; j++) {
                if (matrix[i][j] <= mid) {
                    cnt++;
                }
            }
        }

        if (cnt < k) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }

    return left;
}