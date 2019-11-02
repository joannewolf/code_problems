// Forward declaration of guess API.
// @param num, your guess
// @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
int guess(int num);

class Solution {
public:
    int guessNumber(int n) {
        int l = 1, r = n;
        while (l < r) {
        	int middle = l + (r - l) / 2; // prevent overflow
        	int answer = guess(middle);
        	if (answer == 0)
        		return middle;
        	else if (answer > 0)
        		l = middle + 1;
        	else
        		r = middle - 1;
        }
    	return l;
    }
};