
int compare(const void *a, const void *b) {
    return (**(int **)a - **(int **)b);
}

typedef struct {
    int **schedule;
    int num;
} MyCalendar;


MyCalendar* myCalendarCreate() {
    MyCalendar *obj = calloc(1, sizeof(MyCalendar));
    if (obj == NULL) {
        return NULL;
    }

    obj->schedule = calloc(1000, sizeof(int *));
    if (obj->schedule == NULL) {
        return NULL;
    }

    return obj;
}

bool myCalendarBook(MyCalendar* obj, int start, int end) {
    int i;
    bool sort = true;

    if (obj->num == 0) {
        sort = false;
        goto success;
    }

    if (end <= obj->schedule[0][0]) {
        goto success;
    }

    for (i = 0; i < obj->num-1; i++) {    
        int empty_slot[2];
        
        empty_slot[0] = obj->schedule[i][1];
        empty_slot[1] = obj->schedule[i+1][0];
    
        if (empty_slot[0] <= start && end <= empty_slot[1]) {
            goto success;
        }
    }

    if (obj->schedule[obj->num-1][1] <= start) {
        sort = false;
        goto success;
    }

    return false;
    
success:
    obj->schedule[obj->num] = calloc(2, sizeof(int));
    if (obj->schedule[obj->num] == NULL) {
        return false;
    }

    obj->schedule[obj->num][0] = start;
    obj->schedule[obj->num][1] = end;
    obj->num++;

    if (sort) {
        qsort(obj->schedule, obj->num, sizeof(int *), compare);
    }
    
    return true;
}

void myCalendarFree(MyCalendar* obj) {
    free(obj->schedule);
    free(obj);
}

/**
 * Your MyCalendar struct will be instantiated and called as such:
 * MyCalendar* obj = myCalendarCreate();
 * bool param_1 = myCalendarBook(obj, start, end);
 
 * myCalendarFree(obj);
*/