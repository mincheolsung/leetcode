void swap(char *a, char *b) {
    char temp = *b;
    *b = *a;
    *a = temp;
}

char * thousandSeparator(int n){
    int i, j, left, right;

    if (n == 0) {
        return "0";
    }
    
    char *result = malloc(100*sizeof(char));
    if (result == NULL) {
        return NULL;
    }
    
    i = 0;
    j = 0;
    while (n > 0) {
        result[i++] = ('0' + n%10);
        n /= 10;
        j++;
        if ((j % 3) == 0 && n > 0) {
            result[i++] = '.';
        }
    }
    result[i] = '\0';
      
    left = 0;
    right = i - 1;
    while (left < right) {
        swap(&result[left++], &result[right--]);
    }
    
    return result;
}
