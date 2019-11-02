class Solution {
public:
	string getPermutation(int n, int k) {
		vector<char> unusedNums;
		string result;
		int factorial = 1;

		for (int i = 1; i <= n; i++) {
			unusedNums.push_back(i + '0');
			factorial *= i;
		}

		k -= 1;
		factorial /= unusedNums.size();
		for (int i = 0; i < n - 1; i++) {
			result += unusedNums[k / factorial];
			unusedNums.erase(unusedNums.begin() + (k / factorial));
			k %= factorial;
			factorial /= unusedNums.size();
		}
		result += unusedNums[0];
		return result;
	}
};