class Solution {
public:
    string reverseVowels(string s) {
        vector<int> vowelIndex;
        string vowels = "aeiouAEIOU";
        for (int i = 0; i < s.length(); i++) {
        	if (vowels.find(s[i]) != -1)
        		vowelIndex.push_back(i);
        }

        for (int i = 0; i < vowelIndex.size() / 2; i++) {
        	char temp = s[vowelIndex[i]];
        	s[vowelIndex[i]] = s[vowelIndex[vowelIndex.size() - 1 - i]];
        	s[vowelIndex[vowelIndex.size() - 1 - i]] = temp;
        }
        return s;
    }
};