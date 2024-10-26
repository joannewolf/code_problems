// O(NlogN), compare sorted string
// N: string length
class Solution {
public:
	bool isAnagram(string s, string t) {
		if (s.size() != t.size())
			return false;
		if (s.size() == t.size() && s.size() == 0)
			return true;

		sort(s.begin(), s.end());
		sort(t.begin(), t.end());
		return (s == t);
	}
};

// O(N), compare alphabet count
class Solution {
public:
	bool isAnagram(string s, string t) {
		vector<int> sCount(26, 0);
		vector<int> tCount(26, 0);

		for (char c : s)
			sCount[c - 'a'] ++;
		for (char c : t)
			tCount[c - 'a'] ++;

		for (int i = 0; i < 26; i++) {
			if (sCount[i] != tCount[i])
				return false;
		}
		return true;
	}
};