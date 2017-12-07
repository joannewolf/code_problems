#include <numeric>
class Solution {
private:
	int gcd(int x, int y) {
		return y == 0 ? x : gcd(y, x % y);
	}
public:
    bool canMeasureWater(int x, int y, int z) {
        // check if z is a multiple of GCD(x, y)
        return z == 0 || ((z <= (long long)x + y) && (z % gcd(x, y) == 0));
    }
};