void swap(char *a, char *b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

int partition(char *str, int left, int right) {
    int i,j;
    i = left - 1;
    for (j = left; j < right; j++) {
        if (str[j] < str[right]) {
            i++;
            swap(&str[i], &str[j]);
        }
    }
    swap(&str[i+1], &str[right]);
    return (i+1);
}

void quick_sort(char *str, int left, int right) {
    if (left < right) {
        int piv = partition(str,left,right);
        quick_sort(str, left, piv-1);
        quick_sort(str, piv+1, right);
    }
}

int compare(const void *a, const void *b) {
    if (*(char *)a > *(char *)b) {
        return 1;
    } else if (*(char *)a == *(char *)b) {
        return 0;
    } else {
        return -1;
    }
}

bool isAnagram(char * a, char * b){
    int len_a = strlen(a);
    int len_b = strlen(b);
    int i,j;
    int cnt = 0;

    if (len_a != len_b) {
        return false;
    }
        
    //qsort(a, len_a, sizeof(char), compare);
    //qsort(b, len_b, sizeof(char), compare);
    quick_sort(a, 0, len_a-1);
    quick_sort(b, 0, len_b-1);

    printf("%s %s\n",a,b);
    
    if (strcmp(a,b) == 0) {
        return true;
    }
    
    return false;
}