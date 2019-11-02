// by counting alphabets in sliding window
class Solution {
public:
	vector<int> findAnagrams(string s, string p) {
		vector<int> result;
		vector<int> pCount(26, 0), sCount(26, 0);
		int sLen = s.length(), pLen = p.length();

		for (char c : p)
			pCount[c - 'a'] ++;

		for (int i = 0; i < pLen && i < sLen; i++)
			sCount[s[i] - 'a'] ++;
		for (int i = 0; i <= sLen - pLen; i++) {
			bool isAnagram = true;
			for (int j = 0; j < 26; j++) {
				if (sCount[j] != pCount[j]) {
					isAnagram = false;
					break;
				}
			}
			if (isAnagram)
				result.emplace_back(i);

			sCount[s[i] - 'a'] --;
			sCount[s[i + p.length()] - 'a'] ++;
		}

		return result;
	}
};