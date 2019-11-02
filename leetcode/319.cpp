#include <math.h>
class Solution {
public:
    int bulbSwitch(int n) {
        // the bulb will be switched by the times wihch equal the number of its factors
        // the number which has odd factors will be on at the end, those number are square numbers
    	return sqrt(n);
    }
};