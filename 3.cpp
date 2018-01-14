// O(N), use map
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int startIndex = 0, maxLength = 0;
		map<char, int> index;

		for (int i = 0; i < s.length(); i++) {
			if (index.find(s[i]) != index.end())
				startIndex = max(startIndex, index[s[i]] + 1);
			index[s[i]] = i;
			maxLength = max(maxLength, i - startIndex + 1);
		}

		return maxLength;
	}
};

// O(N), use set and two pointers
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		int startIndex = 0, currentIndex = 0;
		int maxLength = 0;
		set<char> chars;

		while (currentIndex < s.length()) {
			if (chars.find(s[currentIndex]) == chars.end()) {
				chars.emplace(s[currentIndex]);
				currentIndex ++;
				maxLength = max(maxLength, (int)chars.size());
			}
			else {
				chars.erase(s[startIndex]);
				startIndex ++;
			}
		}
		return maxLength;
	}
};

// O(N^2), use string.find()
class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		string currentSubstr = "";
		int maxLength = 0;

		for (int i = 0; i < s.length(); i++) {
			int index = currentSubstr.find(s[i]);
			if (index == -1) {
				currentSubstr.push_back(s[i]);
				maxLength = max(maxLength, (int)currentSubstr.length());
			}
			else {
				currentSubstr = currentSubstr.substr(index + 1);
				currentSubstr.push_back(s[i]);
			}
		}

		return maxLength;
	}
};