// O(NKlogK), group by sorted string
// N: # of strings, K: max length of string
class Solution {
public:
	vector<vector<string>> groupAnagrams(vector<string>& strs) {
		map<string, vector<string>> anagrams;

		for (string str : strs) {
			string temp(str);
			sort(temp.begin(), temp.end());
			if (anagrams.find(temp) == anagrams.end())
				anagrams[temp] = vector<string>(1, str);
			else
				anagrams[temp].emplace_back(str);
		}

		vector<vector<string>> result;
		for (auto it = anagrams.begin(); it != anagrams.end(); it ++) {
			result.emplace_back(it -> second);
		}
		return result;
	}
};

// O(NK), group by alphabet count
class Solution {
public:
	vector<vector<string>> groupAnagrams(vector<string>& strs) {
		map<string, vector<string>> anagrams;

		for (string str : strs) {
			vector<int> alphabetCount(26, 0);
			for (char c : str)
				alphabetCount[c - 'a'] ++;
			string key = "";
			for (int i = 0; i < 26; i++)
				key += ("#" + to_string(alphabetCount[i]));

			if (anagrams.find(key) == anagrams.end())
				anagrams[key] = vector<string>(1, str);
			else
				anagrams[key].emplace_back(str);
		}

		vector<vector<string>> result;
		for (auto it = anagrams.begin(); it != anagrams.end(); it ++) {
			result.emplace_back(it -> second);
		}
		return result;
	}
};