#include <queue>
#include <utility>
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
    	if (grid.size() == 0 || grid[0].size() == 0)
    		return 0;

    	int count = 0;
    	int n = grid.size(), m = grid[0].size();
        for (int i = 0; i < n; i++) {
        	for (int j = 0; j < m; j++) {
        		if (grid[i][j] == '1') {
        			count ++;
        			// do BFS to mark current island
        			queue<pair<int, int>> toBeChecked;
        			toBeChecked.emplace(make_pair(i, j));
        			while (!toBeChecked.empty()) {
        				pair<int, int> current = toBeChecked.front();
        				toBeChecked.pop();
        				if (grid[current.first][current.second] == '1') {
        					grid[current.first][current.second] = 'a';
        					if (current.first != 0)
	        					toBeChecked.emplace(make_pair(current.first - 1, current.second));
	        				if (current.first != n - 1)
	        					toBeChecked.emplace(make_pair(current.first + 1, current.second));
	        				if (current.second != 0)
	        					toBeChecked.emplace(make_pair(current.first, current.second - 1));
	        				if (current.second != m - 1)
	        					toBeChecked.emplace(make_pair(current.first, current.second + 1));
        				}
        			}
        		}
        	}
        }
        
        return count;
    }
};