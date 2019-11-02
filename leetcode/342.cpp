// without loop
class Solution {
public:
    bool isPowerOfFour(int num) {
    	return ((num > 0) && ((num & (num - 1)) == 0) && ((num & 0x55555555) != 0));
        //0x55555555 = 0101 0101 0101 0101 0101 0101 0101 0101 is to get power of 4 instead of power of 2
    }
};

class Solution {
public:
    bool isPowerOfFour(int num) {
    	if (num <= 0)
    		return false;
        while (num != 1) {
        	if (num % 4 != 0)
        		return false;
        	num /= 4;
        }
        return true;
    }
};