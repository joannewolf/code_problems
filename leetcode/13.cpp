class Solution {
public:
	int romanToInt(string s) {
		unordered_map<char, int> nums({ { 'I' , 1 }, { 'V' , 5 }, { 'X' , 10 }, { 'L' , 50 }, { 'C' , 100 }, { 'D' , 500 }, { 'M' , 1000 } });

		int result = nums[s.back()];
		for (int i = s.length() - 2; i >= 0; i--) {
			if (nums[s[i]] < nums[s[i + 1]])
				result -= nums[s[i]];
			else
				result += nums[s[i]];
		}
		return result;
	}
};