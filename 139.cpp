// O(N^2), dynamic programming I
// N: s length, M: # words in wordDict
class Solution {
public:
	bool wordBreak(string s, vector<string>& wordDict) {
		vector<bool> canBeBroken(s.length() + 1, false);
		// canBeBroken[i]: whether s[0 : i - 1] can be broken
		canBeBroken[0] = true;

		for (int i = 1; i <= s.length(); i++) {
			for (int j = 0; j < i; j++) {
				if (find(wordDict.begin(), wordDict.end(), s.substr(j, i - j)) != wordDict.end() && canBeBroken[j]) {
					canBeBroken[i] = true;
					break;
				}
			}
		}
		return canBeBroken.back();
	}
};

// O(NM), dynamic programming II
class Solution {
public:
	bool wordBreak(string s, vector<string>& wordDict) {
		vector<bool> canBeBroken(s.length() + 1, false);
		// canBeBroken[i]: whether s[0 : i - 1] can be broken
		canBeBroken[0] = true;

		for (int i = 1; i <= s.length(); i++) {
			for (string word : wordDict) {
				if (i >= word.length() && s.substr(i - word.length(), word.length()) == word && canBeBroken[i - word.length()]) {
					canBeBroken[i] = true;
					break;
				}
			}
		}
		return canBeBroken.back();
	}
};

// O(N^2), BFS
class Solution {
public:
	bool wordBreak(string s, vector<string>& wordDict) {
		stack<int> st;
		int n = s.length();
		vector<int> checked(n, false);

		st.push(0);
		while (!st.empty()) {
			int temp = st.top();
			st.pop();
			if (temp == n)
				return true;
			else if (temp > n || checked[temp])
				continue;

			for (string word : wordDict) {
				if (s.substr(temp, word.length()) == word) {
					checked[temp] = true;
					st.push(temp + word.length());
				}
			}
		}

		return false;
	}
};

// O(N^2), recursion with memorization
class Solution {
private:
	vector<bool> checked, canBeBroken;
	vector<string> wordDict;
	string s;
	bool wordBreak(int start) {
		if (start == s.length())
			return true;
		if (checked[start])
			return canBeBroken[start];

		checked[start] = true;
		for (int end = start + 1; end <= s.length(); end ++) {
			if (find(wordDict.begin(), wordDict.end(), s.substr(start, end - start)) != wordDict.end() && wordBreak(end)) {
				canBeBroken[start] = true;
				break;
			}
		}

		return canBeBroken[start];
	}
public:
	bool wordBreak(string s, vector<string>& wordDict) {
		checked = vector<bool>(s.length(), false);
		canBeBroken = vector<bool>(s.length(), false);
		this -> s = s;
		this -> wordDict = wordDict;
		return wordBreak(0);
	}
};