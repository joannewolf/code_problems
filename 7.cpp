#include <stdlib.h>
#include <climits>
class Solution {
public:
    int reverse(int x) {
        int symbol = (x > 0) ? 1 : -1; // 1 for positive, -1 for negative
        x = abs(x);
        long long result = 0;
        while (x != 0) {
        	result = result * 10 + (x % 10);
        	x /= 10;
        }
        result *= symbol;
        if (result > INT_MAX || result < INT_MIN)
        	result = 0;

        return result;
    }
};