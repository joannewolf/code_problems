class Solution {
public:
    int countNumbersWithUniqueDigits(int n) {
        if (n == 0)
        	return 1;
        else {
        	int sum = 10, flag = 9;
        	for (int i = 2; i <= min(n, 10); i++) {
        		flag *= (11 - i);
        		sum += flag;
        	}
        	return sum;
        }
    }
};