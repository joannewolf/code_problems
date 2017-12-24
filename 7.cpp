class Solution {
public:
	int reverse(int x) {
		int symbol = (x > 0) ? 1 : -1; // 1 for positive, -1 for negative
		long long num = abs((long long)x);
		long long result = 0;
		while (num != 0) {
			result = result * 10 + (num % 10);
			num /= 10;
		}
		result *= symbol;
		return (result > INT_MAX || result < INT_MIN) ? 0 : result;
	}
};