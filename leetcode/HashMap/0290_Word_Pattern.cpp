#include <map>
#include <string>
class Solution {
public:
    bool wordPattern(string pattern, string str) {
        vector<string> patterns (26, "");
        
        for (int i = 0; i < pattern.length(); i++) {
        	if (str.length() == 0) // no more words
        		return false;
        	// cut down the word
        	string temp;
        	if (str.find(' ') != -1) {
        		temp = str.substr(0, str.find(' '));
        		str = str.substr(str.find(' ') + 1);
        	}
        	else {
        		temp = str;
        		str = "";
        	}

        	if (patterns[pattern[i] - 97] == "")
        		patterns[pattern[i] - 97] = temp;
        	else if (patterns[pattern[i] - 97] != temp)
        		// check if same pattern match same word
        		return false;
        }
        if (str.length() != 0) // too many words
        	return false;

        // check if multiple patterns share same word
        sort(patterns.begin(), patterns.end());
        for (int i = 1; i < patterns.size(); i++) {
        	if (patterns[i].length() != 0 && patterns[i] == patterns[i - 1])
        		return false;
        }
        return true;
    }
};