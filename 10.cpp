class Solution {
public:
    bool isMatch(string s, string p) {
        int sLen = s.length(), pLen = p.length();
        vector<vector<bool>> DP(sLen + 1, vector<bool>(pLen + 1, false));
        // DP(i, j): isMatch(s[0 : i - 1], p[0 : j - 1])
        
        DP[0][0] = true;
        for (int j = 1; j <= pLen; j++) {
        	if (p[j - 1] == '*')
            	DP[0][j] = DP[0][j - 2];
        }
        
        for (int i = 1; i <= sLen; i++) {
            for (int j = 1; j <= pLen; j++) {
                if (p[j - 1] == '*') {
                	if (p[j - 2] == '.' || s[i - 1] == p[j - 2])
                		// s[i] can be part of * or not
                		DP[i][j] = DP[i - 1][j] || DP[i][j - 2];
                	else
                		DP[i][j] = DP[i][j - 2];
                }
                else {
                    if (p[j - 1] == '.' || s[i - 1] == p[j - 1])
                        DP[i][j] = DP[i - 1][j - 1];
                    // else
                    //     DP[i][j] = false;
                }
            }
        }

        return DP[sLen][pLen];
    }
};