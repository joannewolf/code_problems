class Solution {
public:
    bool isMatch(string s, string p) {
        int sFlag = 0, pFlag = 0;
        while (sFlag < s.length() && pFlag < p.length()) {
            if (p[pFlag + 1] == '*') {
                if (p[pFlag] == '.' || s[sFlag] == p[pFlag])
                	// s[sFlag] can be part of the * or not
                	return (isMatch(s.substr(sFlag + 1), p.substr(pFlag)) || isMatch(s.substr(sFlag), p.substr(pFlag + 2)));
                else 
                    pFlag += 2;
            }
            else {
                if (p[pFlag] == '.' || s[sFlag] == p[pFlag]) {
                    pFlag ++;
                    sFlag ++;
                }
                else
                    return false;
            }
        }
        while (sFlag == s.length() && pFlag < p.length() && p[pFlag + 1] == '*')
        	pFlag += 2;

        return (sFlag == s.length() && pFlag == p.length());
    }
};