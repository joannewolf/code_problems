// O(NM), Vertical Matching, compare 1 character in all strings at a time
// N: # of strings, M: length of strings
class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0)
			return "";

		string prefix = "";
		int flag = 0;
		while (1) {
			for (int i = 0; i < strs.size(); i++) {
				if (flag > strs[i].length() || strs[i][flag] != strs[0][flag])
					return prefix;
			}
			prefix.push_back(strs[0][flag]);
			flag ++;
		}
		return prefix;
	}
};

// O(NM), Horizontal Matching, compare 2 strings at a time
class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0)
			return "";

		string prefix = strs[0];
		for (int i = 1; i < strs.size(); i++) {
			for (int j = 0; j < prefix.length(); j++) {
				if (j == strs[i].length() || prefix[j] != strs[i][j]) {
					prefix = prefix.substr(0, j);
					break;
				}
			}
		}
		return prefix;
	}
};

// O(NM), Divide and Conquer, divide into 2 groups of strings
class Solution {
private:
	vector<string> strs;
	string longestCommonPrefix(int start, int end) {
		if (start == end)
			return strs[start];
		else {
			int middle = (start + end) / 2;
			string lcpLeft = longestCommonPrefix(start, middle);
			string lcpRight = longestCommonPrefix(middle + 1, end);
			
			// find lcp of sub-results
			for (int i = 0; i < min(lcpLeft.length(), lcpRight.length()); i++) {
				if (lcpLeft[i] != lcpRight[i])
					return lcpLeft.substr(0, i);
			}
			return (lcpLeft.length() < lcpRight.length()) ? lcpLeft : lcpRight;
		}
	}

public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0)
			return "";

		this -> strs = strs;
		return longestCommonPrefix(0, strs.size() - 1);
	}
};

// O(NMlogM), Binary Search
class Solution {
private:
	vector<string> strs;
	bool isCommonPrefix(int start, int end) {
		// only need to check the substr between start and end in every string
		int len = end - start + 1;
		for (int i = 1; i < strs.size(); i++) {
			if (strs[0].substr(start, len) != strs[i].substr(start, len))
				return false;
		}
		return true;
	}

public:
	string longestCommonPrefix(vector<string>& strs) {
		if (strs.size() == 0)
			return "";

		this -> strs = strs;
		int minLen = INT_MAX;
		for (string str : strs)
			minLen = min(minLen, (int)str.length());

		int l = 0, r = minLen - 1;
		while (l <= r) {
			int middle = (l + r) / 2;
			if (isCommonPrefix(l, middle))
				l = middle + 1;
			else
				r = middle - 1;
		}

		return strs[0].substr(0, l);
	}
};