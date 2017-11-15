class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        const int live = 1, dead = 0, liveToDead = 2, deadToLive = -1;
        int n = board.size(), m = board[0].size();
        
        for (int i = 0; i < n; i++) {
        	for (int j = 0; j < m; j++) {
        		// calculate live neighbors
        		int liveNeighbors = 0;
        		if (i != 0 && (board[i - 1][j] == live || board[i - 1][j] == liveToDead))
        			liveNeighbors ++;
        		if (i != 0 && j != 0 && (board[i - 1][j - 1] == live || board[i - 1][j - 1] == liveToDead))
        			liveNeighbors ++;
        		if (j != 0 && (board[i][j - 1] == live || board[i][j - 1] == liveToDead))
        			liveNeighbors ++;
        		if (i != n - 1 && j != 0 && (board[i + 1][j - 1] == live || board[i + 1][j - 1] == liveToDead))
        			liveNeighbors ++;
        		if (i != n - 1 && (board[i + 1][j] == live || board[i + 1][j] == liveToDead))
        			liveNeighbors ++;
        		if (i != n - 1 && j != m - 1 && (board[i + 1][j + 1] == live || board[i + 1][j + 1] == liveToDead))
        			liveNeighbors ++;
        		if (j != m - 1 && (board[i][j + 1] == live || board[i][j + 1] == liveToDead))
        			liveNeighbors ++;
        		if (i != 0 && j != m - 1 && (board[i - 1][j + 1] == live || board[i - 1][j + 1] == liveToDead))
        			liveNeighbors ++;

        		if (board[i][j] == 1 && (liveNeighbors < 2 || liveNeighbors > 3)) {
        			board[i][j] = liveToDead;
        		}
        		else if (board[i][j] == 0 && liveNeighbors == 3){
        			board[i][j] = deadToLive;
        		}
        	}
        }

        for (int i = 0; i < n; i++) {
        	for (int j = 0; j < m; j++) {
        		if (board[i][j] == liveToDead)
        			board[i][j] = dead;
        		else if (board[i][j] == deadToLive)
        			board[i][j] = live;
        	}
        }
    }
};