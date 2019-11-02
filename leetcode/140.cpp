// can use either string or vector<int> to represent a string
// moreover, can use another map<char, vector<string>> to speed up the wordDict look up

// O(NM), dynamic programming, both will TLE
class Solution {
public:
	vector<string> wordBreak(string s, vector<string>& wordDict) {
		vector<vector<string>> brokenString(s.length() + 1);
		// brokenString: all word combination of s[0 : i - 1]
		brokenString[0] = vector<string>({""});

		for (int i = 1; i <= s.length(); i++) {
			for (string word : wordDict) {
				if (i >= word.length() && s.substr(i - word.length(), word.length()) == word) {
					for (string temp : brokenString[i - word.length()]) {
						brokenString[i].emplace_back(temp + word + " ");
					}
				}
			}
		}
		for (string &temp : brokenString.back())
			temp.pop_back();
		return brokenString.back();
	}
};

class Solution {
public:
	vector<string> wordBreak(string s, vector<string>& wordDict) {
		vector<vector<vector<int>>> brokenString(s.length() + 1);
		// brokenString: all word combination of s[0 : i - 1]
		brokenString[0] = vector<vector<int>>(1);

		for (int i = 1; i <= s.length(); i++) {
			for (int j = 0; j < wordDict.size(); j++) {
				if (i >= wordDict[j].length() && s.substr(i - wordDict[j].length(), wordDict[j].length()) == wordDict[j]) {
					for (vector<int> wordIndices : brokenString[i - wordDict[j].length()]) {
						wordIndices.emplace_back(j);
						brokenString[i].emplace_back(wordIndices);
					}
				}
			}
		}

		vector<string> result;
		for (vector<int> wordIndices : brokenString.back()) {
			string temp = "";
			for (int wordIndex : wordIndices)
				temp += (wordDict[wordIndex] + " ");
			temp.pop_back();
			result.emplace_back(temp);
		}
		return result;
	}
};

// O(N^2), recursion with memorization
class Solution {
private:
	vector<vector<vector<int>>> brokenString;
	// brokenString[i] records all word combination of s.substr(i)
	vector<bool> checked;
	vector<string> wordDict;
	string s;
	vector<vector<int>> wordBreak(int start) {
		if (start == s.length())
			return vector<vector<int>>(1);
		if (checked[start])
			return brokenString[start];

		checked[start] = true;
		for (int end = start + 1; end <= s.length(); end ++) {
			auto it = find(wordDict.begin(), wordDict.end(), s.substr(start, end - start));
			if (it != wordDict.end()) {
				vector<vector<int>> tempResult = wordBreak(end);
				for (vector<int> &wordIndices : tempResult) {
					wordIndices.insert(wordIndices.begin(), it - wordDict.begin());
					brokenString[start].emplace_back(wordIndices);
				}
			}
		}

		return brokenString[start];
	}
public:
	vector<string> wordBreak(string s, vector<string>& wordDict) {
		checked = vector<bool>(s.length(), false);
		brokenString = vector<vector<vector<int>>>(s.length());
		this -> s = s;
		this -> wordDict = wordDict;

		vector<vector<int>> tempResult = wordBreak(0);
		vector<string> result;
		for (vector<int> wordIndices : tempResult) {
			string temp = "";
			for (int wordIndex : wordIndices)
				temp += (wordDict[wordIndex] + " ");
			temp.pop_back();
			result.emplace_back(temp);
		}
		return result;
	}
};
