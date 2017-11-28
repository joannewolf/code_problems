class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        int n = M.size(), m = M[0].size();
        vector<vector<int>> result(n, vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
        	for (int j = 0; j < m; j++) {
        		int count = 1, sum = M[i][j];
        		if (i != 0) {
        			count ++;
        			sum += M[i - 1][j];
        		}
        		if (i != 0 && j != 0) {
        			count ++;
        			sum += M[i - 1][j - 1];
        		}
        		if (j != 0) {
        			count ++;
        			sum += M[i][j - 1];
        		}
        		if (i != n - 1 && j != 0) {
        			count ++;
        			sum += M[i + 1][j - 1];
        		}
        		if (i != n - 1) {
        			count ++;
        			sum += M[i + 1][j];
        		}
        		if (i != n - 1 && j != m - 1) {
        			count ++;
        			sum += M[i + 1][j + 1];
        		}
        		if (j != m - 1) {
        			count ++;
        			sum += M[i][j + 1];
        		}
        		if (i != 0 && j != m - 1) {
        			count ++;
        			sum += M[i - 1][j + 1];
        		}
        		result[i][j] = floor(sum / count);
        	}
        }

        return result;
    }
};