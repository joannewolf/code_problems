class Solution {
private:
	static bool sortStrByLength(string a, string b) {
		if (a.length() != b.length())
			return (a.length() > b.length());
		else
			return (a < b);
	}
public:
    string findLongestWord(string s, vector<string>& d) {
        if (s.length() == 0 || d.size() == 0)
        	return "";

        sort(d.begin(), d.end(), sortStrByLength);
        for (string str : d) {
        	int flagDict = 0, flagStr = 0;
        	while (flagDict < s.length() && flagStr < str.length()) {
        		if (s[flagDict] == str[flagStr]) {
        			flagDict ++;
        			flagStr ++;
        		}
        		else
        			flagDict ++;
        	}
        	if (flagStr == str.length())
        		return str;
        }
        return "";
    }
};