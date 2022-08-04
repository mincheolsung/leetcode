/*
    0 1 2 0 1 2
    
    0 1 2 3 0 0 0 0

*/

int timeRequiredToBuy(int* tickets, int ticketsSize, int k){
    int i = 0;
    int result = 0;
    while (1) {
        if (tickets[i] > 0) {
            result++;
            tickets[i]--;
            if (k == i && tickets[i] == 0) {
                return result;
            }
        }
        i = (i+1)%ticketsSize;
    }

    return 0;
}