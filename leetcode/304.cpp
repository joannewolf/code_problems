	class NumMatrix {
	private:
		vector<vector<int>> sum;
	public:
	    NumMatrix(vector<vector<int>> matrix) {
	        // for every element(i, j) in matrix, calculate the sum of region(0, 0, i, j)
	        if (matrix.size() == 0 || matrix[0].size() == 0)
	        	return;
	        int n = matrix.size(), m = matrix[0].size();
	        sum = vector<vector<int>>(n, vector<int>(m, 0));
	        sum[0][0] = matrix[0][0];
	        for (int i = 1; i < n; i++)
	        	sum[i][0] = sum[i - 1][0] + matrix[i][0];
	        for (int i = 1; i < m; i++)
	        	sum[0][i] = sum[0][i - 1] + matrix[0][i];
	        for (int i = 1; i < n; i++) {
	        	for (int j = 1; j < m; j++)
	        		sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + matrix[i][j];
	        }
	    }
	    
	    int sumRegion(int row1, int col1, int row2, int col2) {
	    	int result = sum[row2][col2];
	    	result -= ((row1 == 0) ? 0 : sum[row1 - 1][col2]);
	    	result -= ((col1 == 0) ? 0 : sum[row2][col1 - 1]);
	    	result += ((row1 == 0 || col1 == 0) ? 0 : sum[row1 - 1][col1 - 1]);
	    	return result;
	    }
	};

	/**
	 * Your NumMatrix object will be instantiated and called as such:
	 * NumMatrix obj = new NumMatrix(matrix);
	 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
	 */