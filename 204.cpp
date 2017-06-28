class Solution {
public:
    int countPrimes(int n) {
        if (n <= 2)
            return 0;
        vector<bool> primes(n, true);
        int count = 0;
        for (int i = 2; i * i < n; i++) {
            if (primes[i]) {
                // mark false to all multiples of this prime, can start check from i*i, i*i + i, ...
                for (int j = 0; i * (i + j) < n; j++)
                    primes[i * (i + j)] = false;
            }
        }

        for (int i = 2; i < n; i++) {
            if (primes[i])
                count ++;
        }
        return count;
    }
};