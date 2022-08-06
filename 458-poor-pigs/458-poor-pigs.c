int poorPigs(int buckets, int minutesToDie, int minutesToTest){
    int tests_per_pig = minutesToTest/minutesToDie + 1;
    int num_of_pigs = 0;
    int total_tests = 1;
    
    while (total_tests < buckets) {
        total_tests = total_tests*tests_per_pig;
        num_of_pigs++;
    }

    return num_of_pigs;
}