bool match(char *word, char *pattern) {
    int i,j;
    int len;
    char *dict;

    len = strlen(pattern);
    if (len == 1) {
        return true;
    }
    
    dict = calloc(26, sizeof(char));
    if (dict == NULL) {
        return false;
    }
        
    for (i = 0; i < len; i++) {
        if (dict[pattern[i]-'a'] == 0) {
            for (j = 0; j < 26; j++) {
                if (dict[j] == word[i]) {
                    return false;
                }
            }
            dict[pattern[i]-'a'] = word[i];     
        } else {
            if (dict[pattern[i]-'a'] != word[i]) {
                return false;
            }
        }
    }
    
    return true;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char ** findAndReplacePattern(char ** words, int wordsSize, char * pattern, int* returnSize){
    int i, idx;
    char **result;
    
    *returnSize = 0;
    result = calloc(wordsSize, sizeof(char *));
    if (result == NULL) {
        return NULL;
    }
    
    idx = 0;
    for (i = 0; i < wordsSize; i++) {
        if (match(words[i], pattern)) {
            result[idx++] = words[i];
        }
    }

    result = realloc(result, idx*sizeof(char *));
    if (result == NULL) {
        return NULL;
    }

    *returnSize = idx;
    return result;
}