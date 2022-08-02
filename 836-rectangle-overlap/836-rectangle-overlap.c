/*
    (x1 y2)   (x2 y2)
    
    (x1 y1)   (x2 y1)
*/

#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)


bool isRectangleOverlap(int* rec1, int rec1Size, int* rec2, int rec2Size){
    int *p1;
    int *p2;
    
    if (rec1[0] < rec2[0]) {
        p1 = rec1;
        p2 = rec2;
    } else {
        p1 = rec2;
        p2 = rec1;
    }
    
    if (p1[2] <= p2[0]) {
        return false;
    }
    
    if (p1[3] < p2[1] || p1[1] > p2[3]) {
        return false;
    }
    
    return true;
}