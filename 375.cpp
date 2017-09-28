#include <math.h>
class Solution {
public:
    int getMoneyAmount(int n) {
        vector<vector<int>> money(n + 1, vector<int>(n + 1, INT_MAX));
        // money[i][j]: guess number between [i, j], the guaranteed amount of money to win

        for (int i = 1; i <= n; i++)
        	money[i][i] = 0;
        for (int i = n - 1; i >= 1; i--) {
        	for (int j = i + 1; j <= n; j++) {
        		// in range [i, j], try every guess and find the minimum money
        		money[i][j] = min(money[i][j], i + money[i + 1][j]);
        		for (int k = i + 1; k < j; k++)
        			money[i][j] = min(money[i][j], k + max(money[i][k - 1], money[k + 1][j]));
        		money[i][j] = min(money[i][j], money[i][j - 1] + j);
        	}
        }
        return money[1][n];
    }
};