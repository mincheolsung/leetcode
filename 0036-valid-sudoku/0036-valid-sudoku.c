bool is_valid(char *chars) {
    int dict[9] = {0};
    
    for (int i = 0; i < 9; i++) {
        if (chars[i] == '.') {
            continue;
        }
        if (dict[chars[i] - '1'] == 0) {
            dict[chars[i] - '1']++;
        } else {
            return false;
        }
    }

    return true;
}

bool isValidSudoku(char** board, int boardSize, int* boardColSize){
    int i,j,h,k;
    int index;
    char temp[9];

    for (i = 0; i < 9; i++) {    
        { /* check a row */
            if (!is_valid(board[i])) {
                return false;
            }
        }
        
        { /* check a col */
            index = 0;
            for (j = 0; j < 9; j++) {
                 temp[index++] = board[j][i];   
            }
            if (!is_valid(temp)) {
                return false;
            }
        }
        
        /* check a sub-box */
        if ((i%3) == 0) {
            for (j = 0; j < 9; j+= 3) {
                k = 0;
                h = 0;
                index = 0;
                while (index < 9) {
                    temp[index++] = board[i+k][j+h];
                    k++;
                    h += k/3;
                    k %= 3;
                }
                if (!is_valid(temp)) {
                    return false;
                }
            }
        }
    }
    
    return true;
}