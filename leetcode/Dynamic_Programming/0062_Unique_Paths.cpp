class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m <= 0 || n <= 0)
            return 0;
        vector<vector<int>> pathCounts(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++)
            pathCounts[i][n - 1] = 1;
        for (int i = 0; i < n; i++)
            pathCounts[m - 1][i] = 1;
        for (int i = m - 2; i >= 0; i--) {
            for (int j = n - 2; j >= 0; j--)
                pathCounts[i][j] = pathCounts[i + 1][j] + pathCounts[i][j + 1];
        }

        return pathCounts[0][0];
    }
};