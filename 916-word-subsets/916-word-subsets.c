#define max(a,b) (a>b?a:b)

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** wordSubsets(char ** words1, int words1Size, char ** words2, int words2Size, int* returnSize){
    int i,j,idx;
    int k;
    int dict_origin[26] = {0};
    int dict_copy[26] = {0};
    
    char **result;

    *returnSize = 0;    
    result = calloc(words1Size, sizeof(char *));
    if (result == NULL) {
        return NULL;
    }

    idx = 0;
    for (j = 0; j < words2Size; j++) {
        for (k = 0; k < strnlen(words2[j], 10); k++) {
            dict_copy[words2[j][k] - 'a']++;
        }
        
        for (k = 0; k < 26; k++) {
            dict_origin[k] = max(dict_origin[k], dict_copy[k]);
            dict_copy[k] = 0;
        }
    }

    for (i = 0; i < words1Size; i++) {
        for (k = 0; k < 26; k++) {
            dict_copy[k] = dict_origin[k];
        }

        for (k = 0; k < strnlen(words1[i], 10); k++) {
            if (dict_copy[words1[i][k] - 'a'] > 0) {
                dict_copy[words1[i][k] - 'a']--;
            }
        }

        for (k = 0; k < 26; k++) {
            if (dict_copy[k] != 0) {
                goto loop_out;
            }
        }
        result[idx++] = words1[i];
loop_out:
        ;
    }

    result = realloc(result, sizeof(char *)*idx);
    if (result == NULL) {
        return NULL;
    }
    
    *returnSize = idx;
    return result;
}