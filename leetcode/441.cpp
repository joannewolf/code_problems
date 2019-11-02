#include <math.h>
class Solution {
public:
    int arrangeCoins(int n) {
        // (1 + r) * r / 2 <= n, find the largest r
        double r = sqrt(2) * sqrt(n);

        return ((1 + (long long)r) * (long long)r / 2 <= (long long)n) ? (int)r : (int)(r - 1);
    }
};