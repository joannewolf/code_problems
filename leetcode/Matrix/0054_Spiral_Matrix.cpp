#include <algorithm>
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> result;
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return result;

        vector<vector<bool>> checked(matrix.size(), vector<bool>(matrix[0].size(), false));
        int curR = 0, curC = 0, m = matrix.size(), n = matrix[0].size(), count = 0;
        int direction = 0; // 0: right, 1: down, 2: left, 3: up
        while (count < m * n) {
            result.push_back(matrix[curR][curC]);
            checked[curR][curC] = true;
            count ++;
            switch(direction) {
                case 0:
                    if (curC == n - 1 || checked[curR][curC + 1] == true) {
                        curR ++;
                        direction = 1;
                    }
                    else
                        curC ++;
                    break;
                case 1:
                    if (curR == m - 1 || checked[curR + 1][curC] == true) {
                        curC --;
                        direction = 2;
                    }
                    else
                        curR ++;
                    break;
                case 2:
                    if (curC == 0 || checked[curR][curC - 1] == true) {
                        curR --;
                        direction = 3;
                    }
                    else
                        curC --;
                    break;
                case 3:
                    if (curR == 0 || checked[curR - 1][curC] == true) {
                        curC ++;
                        direction = 0;
                    }
                    else
                        curR --;
                    break;
            }
        }
        return result;
    }
};