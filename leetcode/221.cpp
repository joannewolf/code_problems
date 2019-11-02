class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0)
        	return 0;
        int n = matrix.size(), m = matrix[0].size(), maxSquare = 0, consecutiveOnesRow = 0;
        vector<vector<int>> squares(n, vector<int>(m, 0));
        vector<int> consecutiveOnesColumn(m, 0);

        for (int i = 0; i < n; i++) {
        	squares[i][0] = matrix[i][0] - 48;
   			maxSquare = max(maxSquare, squares[i][0]);
        }
        for (int i = 0; i < m; i++) {
        	squares[0][i] = matrix[0][i] - 48;
        	consecutiveOnesColumn[i] = squares[0][i];
   			maxSquare = max(maxSquare, squares[0][i]);
        }
        for (int i = 1; i < n; i++) {
        	consecutiveOnesRow = squares[i][0];
        	for (int j = 1; j < m; j++) {
        		if (matrix[i][j] == '1') {
        			squares[i][j] = min(min(squares[i - 1][j - 1], consecutiveOnesRow), consecutiveOnesColumn[j]) + 1;
        			consecutiveOnesRow ++;
        			consecutiveOnesColumn[j] ++;
        			maxSquare = max(maxSquare, squares[i][j]);
        		}
        		else {
        			consecutiveOnesRow = 0;
        			consecutiveOnesColumn[j] = 0;
        		}
        	}
        }

        return (maxSquare * maxSquare);
    }
};