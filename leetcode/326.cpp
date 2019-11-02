// without loop
class Solution {
public:
    bool isPowerOfThree(int n) {
        // 1162261467 = 3^19, 3^20 will overflow
        return (n > 0 && 1162261467 % n == 0);
    }
};

class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0)
        	return false;
        while (n != 1) {
        	if (n % 3 != 0)
        		return false;
        	n /= 3;
        }
        return true;
    }
};