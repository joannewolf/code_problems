class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
        	return;

        int m = matrix.size(), n = matrix[0].size();
        // use first row/column to record which row/column need to be zeroed
        bool zeroFirstRow = false, zeroFirstColumn = false;

        // record the row/column that need to be zeroed
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    zeroFirstRow |= (j == 0);
                    zeroFirstColumn |= (i == 0);
                    matrix[0][j] = 0;
                    matrix[i][0] = 0;
                }
            }
        }

        // fill in zeros
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[0][j] == 0 || matrix[i][0] == 0)
                    matrix[i][j] = 0;
            }
        }
        if (zeroFirstRow) {
            for (int i = 0; i < m; i++)
                matrix[i][0] = 0;
        }
        if (zeroFirstColumn) {
            for (int i = 0; i < n; i++)
                matrix[0][i] = 0;
        }
    }
};