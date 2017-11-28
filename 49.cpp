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