#include <algorithm>
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> form(m + 1, vector<int>(n + 1, 0));
        // form[i][j]: with i zeros and j ones, the maximum # of strings can be formed
        for (string s : strs) {
        	int zeros = 0, ones = 0;
        	for (char c : s) {
        		if (c == '0')
        			zeros ++;
        		else if (c == '1')
        			ones ++;
        	}

        	for (int i = m; i >= zeros; i--) {
        		for (int j = n; j >= ones; j--) {
        			form[i][j] = max(form[i][j], form[i - zeros][j - ones] + 1);
        		}
        	}
        }
        return form[m][n];
    }
};