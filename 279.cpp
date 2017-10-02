#include <climits>
class Solution {
public:
    int numSquares(int n) {
        vector<int> combinations(n + 1, INT_MAX);
        combinations[0] = 0;
        for (int i = 1; i <= n; i++) {
        	for (int j = 1; i - (j * j) >= 0; j++)
        		combinations[i] = min(combinations[i], combinations[i - j * j] + 1);
        }

        return combinations.back();
    }
};