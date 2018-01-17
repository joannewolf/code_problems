// O(N), O(N) space, storing consecutive groups
class Solution {
public:
	int countBinarySubstrings(string s) {
		if (s.empty())
			return 0;

		// count consecutive 0's or 1's
		vector<int> digitCount;
		int count = 1;
		for (int i = 1; i < s.length(); i++) {
			if (s[i] == s[i - 1])
				count ++;
			else {
				digitCount.emplace_back(count);
				count = 1;
			}
		}
		digitCount.emplace_back(count);

		int result = 0;
		for (int i = 1; i < digitCount.size(); i++)
			result += min(digitCount[i - 1], digitCount[i]);
		return result;
	}
};

// O(N), O(1) space, calculate answer on the fly
class Solution {
public:
	int countBinarySubstrings(string s) {
		if (s.empty())
			return 0;

		// count consecutive 0's or 1's
		int result = 0;
		int previous = 0, current = 1;
		for (int i = 1; i < s.length(); i++) {
			if (s[i] == s[i - 1])
				current ++;
			else {
				result += min(previous, current);
				previous = current;
				current = 1;
			}
		}
		return result + min(previous, current);
	}
};