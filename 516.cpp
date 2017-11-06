#include <algorithm>
class Solution {
public:
    int longestPalindromeSubseq(string s) {
    	if (s.empty())
    		return 0;
    	int n = s.length();
        vector<vector<int>> palindromeSubseq(n, vector<int>(n, 0));
        // palindromeSubseq[i][j]: the length of longest palindrome subsequence between s[i] and s[j]

        for (int i = 0; i < n; i++) {
        	palindromeSubseq[i][i] = 1;
        }
        for (int i = 0; i < n - 1; i++) {
        	palindromeSubseq[i][i + 1] = (s[i] == s[i + 1]) ? 2 : 1;
        }
        for (int range = 3; range <= n; range ++) {
        	for (int start = 0; start <= n - range; start ++) {
        		int end = start + range - 1;
        		palindromeSubseq[start][end] = max(palindromeSubseq[start][end - 1], palindromeSubseq[start + 1][end]);
        		if (s[start] == s[end])
        			palindromeSubseq[start][end] = max(palindromeSubseq[start][end], palindromeSubseq[start + 1][end - 1] + 2);
        	}
        }
        return palindromeSubseq[0][n - 1];
    }
};