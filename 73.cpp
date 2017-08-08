class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
        	return;

        int m = matrix.size(), n = matrix[0].size();
        vector<int> zeroRow(m, 1), zeroColumn(n, 1);
        
        // record all row and column that need to be zeroed
        for (int i = 0; i < m; i++) {
        	for (int j = 0; j < n; j++) {
        		if (matrix[i][j] == 0) {
        			zeroRow[i] = 0;
        			zeroColumn[j] = 0;	
        		}
        	}
        }

        // fill in zeros
        for (int i = 0; i < m; i++) {
        	for (int j = 0; j < n; j++) {
        		if (zeroRow[i] == 0 || zeroColumn[j] == 0)
        			matrix[i][j] = 0;
        	}
        }
    }
};