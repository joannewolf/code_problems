#include <limits>
class Solution {
public:
    double myPow(double x, int n) {
    	if (n == 0 || x == 1)
    		return 1;
    	if (x == 0)
    		return (n > 0) ? 0 : numeric_limits<double>::max();

    	vector<double> multiples;
    	multiples.push_back(1);
    	multiples.push_back(x);
        double result = 1;
        long long temp = 2, longN = (long long)n;
        int flag = 2;
        
        longN = abs(longN);
        while (temp <= longN) {
        	multiples.push_back(multiples.back() * multiples.back());
        	temp *= 2;
        	flag ++;
        }

        while (longN != 0) {
        	if (temp > longN) {
        		temp /= 2;
        		flag --;
        	}
        	else {
        		result *= multiples[flag];
        		longN -= temp;
        	}
        }
        return (n >= 0) ? result : (1 / result);
    }
};