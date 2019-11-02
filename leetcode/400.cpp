class Solution {
public:
    int findNthDigit(int n) {
        long long digit = 1, count = 9, start = 1;
        while (n > count * digit) {
        	n -= (count * digit);
        	count *= 10;
        	digit ++;
        	start *= 10;
        }
        if (n % digit == 0)
        	return ((n / digit + start - 1) % 10);
        else
        	return (to_string(n / digit + start)[n % digit - 1]) - 48;
    }
};