#include <algorithm>
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> pathSum(m, vector<int>(n, 0));
        pathSum[m - 1][n - 1] = grid[m - 1][n - 1];
        for (int i = m - 2; i >= 0; i--)
            pathSum[i][n - 1] = pathSum[i + 1][n - 1] + grid[i][n - 1];
        for (int i = n - 2; i >= 0; i--)
            pathSum[m - 1][i] = pathSum[m - 1][i + 1] + grid[m - 1][i];
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--)
                pathSum[i][j] = min(pathSum[i + 1][j], pathSum[i][j + 1]) + grid[i][j];
        }

        return pathSum[0][0];
    }
};