class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;
        int perimeter = 0, mapHeight = grid.size(), mapWidth = grid[0].size();
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 0)
                    continue;
                if (i == 0 || grid[i - 1][j] == 0) // up
                    perimeter ++;
                if (j == 0 || grid[i][j - 1] == 0) // left
                    perimeter ++;
                if (i == mapHeight - 1 || grid[i + 1][j] == 0) // down
                    perimeter ++;
                if (j == mapWidth - 1 || grid[i][j + 1] == 0) // right
                    perimeter ++;
            }
        }
        return perimeter;
    }
};