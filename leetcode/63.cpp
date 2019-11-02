class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.size() == 0 || obstacleGrid[0].size() == 0)
            return 0;
        int m = obstacleGrid.size(), n = obstacleGrid[0].size();
        vector<vector<int>> pathCounts(m, vector<int>(n, 0));
        pathCounts[m - 1][n - 1] = (obstacleGrid[m - 1][n - 1] == 1) ? 0 : 1;
        for (int i = m - 2; i >= 0; i--)
            pathCounts[i][n - 1] = (obstacleGrid[i][n - 1] == 1) ? 0 : pathCounts[i + 1][n - 1];
        for (int i = n - 2; i >= 0; i--)
            pathCounts[m - 1][i] = (obstacleGrid[m - 1][i] == 1) ? 0 : pathCounts[m - 1][i + 1];
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--)
                pathCounts[i][j] = (obstacleGrid[i][j] == 1) ? 0 : (pathCounts[i + 1][j] + pathCounts[i][j + 1]);
        }

        return pathCounts[0][0];
    }
};