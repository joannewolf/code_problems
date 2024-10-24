#include <math.h>
class Solution {
public:
    bool isHappy(int n) {
        // 1 ~ 10, only 1 and y are happy number
        while (true) {
            int temp = 0;
            while (n != 0) {
                temp += pow(n % 10, 2);
                n /= 10;
            }
            if (temp == 1 || temp == 7)
                return true;
            else if (temp < 10)
                return false;
            n = temp;
        }
    }
};