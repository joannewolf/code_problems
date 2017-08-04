class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return;
        int n = matrix.size();
        for (int i = 0; i < n / 2; i++) {
            for (int j = i; j < n - 1 - i; j ++) {
                int temp = matrix[n - 1 - j][i]; // down left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]; // move down right to down left
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]; // move up right to down right
                matrix[j][n - 1 - i] = matrix[i][j]; // move up left to up right
                matrix[i][j] = temp; // move down left to up left
            }
        }
    }
};