class Solution {
public:
    bool hasAlternatingBits(int n) {
        bool previousBit = (n % 2);
        n /= 2;

        while (n != 0) {
        	if (n % 2 == previousBit)
        		return false;
        	previousBit = !previousBit;
        	n /= 2;
        }
        return true;
    }
};