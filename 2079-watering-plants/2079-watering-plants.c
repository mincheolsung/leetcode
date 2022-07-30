

int wateringPlants(int* plants, int plantsSize, int capacity){
    int current_water;
    int i;
    int steps = 0;

    current_water = capacity;
    for (i = 0; i < plantsSize; i++) {
retry:
        if (current_water < plants[i]) {
            // Go to river to refill the can
            steps += 2*i;
            current_water = capacity;
            goto retry;
        } else {
            current_water -= plants[i];
            steps++;
        }
    }

    return steps;
}