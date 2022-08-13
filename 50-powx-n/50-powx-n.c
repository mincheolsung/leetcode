double myPow2(double x, int n) {
    if (n == 0) {
        return 1;
    }

    double result = myPow2(x, n/2);
    if (n%2 == 0) {
        return result*result;
    } else {
        return result*result*x;        
    }
}

double myPow(double x, int n) {
    long long N = n;
    if (N < 0) {
        x = 1/x;
        N = -1*N;
    }
    return myPow2(x,N);
}