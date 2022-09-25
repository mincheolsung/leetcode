
typedef struct {
    int *queue;
    int head;
    int tail;
    int size;
} MyCircularQueue;

bool myCircularQueueIsEmpty(MyCircularQueue* obj);
bool myCircularQueueIsFull(MyCircularQueue* obj);

MyCircularQueue* myCircularQueueCreate(int k) {
    MyCircularQueue *my_queue = calloc(1, sizeof(MyCircularQueue));
    my_queue->queue = calloc(k, sizeof(int));
    if (!my_queue->queue) {
        return NULL;
    }
    my_queue->head = my_queue->tail = -1;
    my_queue->size = k;

    return my_queue;
}

bool myCircularQueueEnQueue(MyCircularQueue* obj, int value) {
    if (myCircularQueueIsFull(obj)) {
        return false;
    }
    if (obj->head == -1) {
        obj->head = 0;
        obj->tail = 0;
        obj->queue[obj->head] = value;
        return true;
    }

    obj->head = (obj->head+1)%obj->size;
    obj->queue[obj->head] = value;
    return true;
}

bool myCircularQueueDeQueue(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj)) {
        return false;
    }

    if (obj->head == obj->tail) {
        obj->tail = -1;
        obj->head = -1;
    } else {
        obj->tail = (obj->tail + 1) % obj->size;
    }
    return true;
}

int myCircularQueueFront(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj)) {
        return -1;
    }
    return obj->queue[obj->tail];
}

int myCircularQueueRear(MyCircularQueue* obj) {
    if (myCircularQueueIsEmpty(obj)) {
        return -1;
    }
    return obj->queue[obj->head];
}

bool myCircularQueueIsEmpty(MyCircularQueue* obj) {
    if (obj->head == -1) {
        return true;
    }
    return false;
}

bool myCircularQueueIsFull(MyCircularQueue* obj) {
    if ((obj->head + 1)%obj->size == obj->tail) {
        return true;
    }
    return false;
}

void myCircularQueueFree(MyCircularQueue* obj) {
    free(obj->queue);
    obj->queue = NULL;
}

/**
 * Your MyCircularQueue struct will be instantiated and called as such:
 * MyCircularQueue* obj = myCircularQueueCreate(k);
 * bool param_1 = myCircularQueueEnQueue(obj, value);
 
 * bool param_2 = myCircularQueueDeQueue(obj);
 
 * int param_3 = myCircularQueueFront(obj);
 
 * int param_4 = myCircularQueueRear(obj);
 
 * bool param_5 = myCircularQueueIsEmpty(obj);
 
 * bool param_6 = myCircularQueueIsFull(obj);
 
 * myCircularQueueFree(obj);
*/