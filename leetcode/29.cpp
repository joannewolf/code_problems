#include <climits>
#include <stdlib.h>
class Solution {
public:
    int divide(int dividend, int divisor) {
        long long Dividend = abs((long long)dividend);
        long long Divisor = abs((long long)divisor);
        long long tempSum = Divisor, result = 0, flag = 1;
        int symbol = (dividend > 0) ^ (divisor > 0);
        vector<long long> elements, counts; // divisor * 0, divisor * 1, divisor * 2, divisor * 4, ...
        counts.push_back(0);
        elements.push_back(0);
        while (Dividend >= tempSum) {
            elements.push_back(tempSum);
            counts.push_back(flag);
            tempSum += tempSum;
            flag += flag;
        }

        flag = counts.size() - 1;
        while (Dividend >= Divisor && flag > 0) {
            while (Dividend >= elements[flag]) {
                Dividend -= elements[flag];
                result += counts[flag];
            }
            flag --;
        }
        return (symbol == 0) ? min(result, (long long)INT_MAX) : (-result);
    }
};