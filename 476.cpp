#include <math.h>
class Solution {
public:
    int findComplement(int num) {
        int power = 1;
        while (num >= pow(2, power)) {
            power ++;
        }
        return (pow(2, power) - num - 1);
    }
};