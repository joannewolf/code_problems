class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxArea = 0;
        int n = grid.size(), m = grid[0].size();

        for (int i = 0; i < n; i++) {
        	for (int j = 0; j < m; j++) {
        		if (grid[i][j] == 1) {
        			// fill out all island
        			int currentArea = 0;
        			queue<pair<int, int>> toBeChecked;
        			toBeChecked.emplace(make_pair(i, j));

        			while (!toBeChecked.empty()) {
        				pair<int, int> current = toBeChecked.front();
        				toBeChecked.pop();
        				if (grid[current.first][current.second] == 1) {
        					currentArea ++;
        					grid[current.first][current.second] = -1;

        					if (current.first != 0 && grid[current.first - 1][current.second] == 1)
        					toBeChecked.emplace(make_pair(current.first - 1, current.second));
	        				if (current.first != n - 1 && grid[current.first + 1][current.second] == 1)
	        					toBeChecked.emplace(make_pair(current.first + 1, current.second));
	        				if (current.second != 0 && grid[current.first][current.second - 1] == 1)
	        					toBeChecked.emplace(make_pair(current.first, current.second - 1));
	        				if (current.second != m - 1 && grid[current.first][current.second + 1] == 1)
	        					toBeChecked.emplace(make_pair(current.first, current.second + 1));
        				}
        			}
        			
        			maxArea = max(currentArea, maxArea);
        		}
        	}
        }

        return maxArea;
    }
};