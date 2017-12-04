class Solution {
public:
    string longestWord(vector<string>& words) {
    	int maxWordLength = 30;
        vector<vector<string>> dictionary(maxWordLength + 2);

        for (string word : words) {
        	dictionary[word.length()].emplace_back(word);
        }

        for (int i = 2; i <= maxWordLength + 1; i++) {
        	for (int j = 0; j < dictionary[i].size(); j++) {
        		if (find(dictionary[i - 1].begin(), dictionary[i - 1].end(), dictionary[i][j].substr(0, i - 1)) == dictionary[i - 1].end()) {
        			dictionary[i].erase(dictionary[i].begin() + j);
        			j--;
        		}
        	}
        	if (dictionary[i].empty()) {
        		sort(dictionary[i - 1].begin(), dictionary[i - 1].end());
        		return dictionary[i - 1][0];
        	}
        }
        return "";
    }
};