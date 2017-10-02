#include <math.h>
class Solution {
public:
    int integerBreak(int n) {
        if (n == 1 || n == 2)
        	return 1;
        if (n == 3)
        	return 2;
        if (n == 4)
        	return 4;
        switch(n % 3) {
        	case 0:
        		return pow(3, n / 3);
        	case 1:
        		return 4 * pow(3, (n - 4) / 3);
        	case 2:
        		return 2 * pow(3, (n - 2) / 3);
        }
    }
};