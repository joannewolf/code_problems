class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        if (n <= 0)
            return vector<vector<int>>();
        vector<vector<int>> result(n, vector<int>(n, 0));
        int direction = 0; // 0: right, 1: down, 2: left, 3: up
        int count = 1, curR = 0, curC = 0;
        while (count <= n * n) {
            result[curR][curC] = count;
            switch(direction) {
                case 0:
                    if (curC == n - 1 || result[curR][curC + 1] != 0) {
                        curR ++;
                        direction = 1;
                    }
                    else
                        curC ++;
                    break;
                case 1:
                    if (curR == n - 1 || result[curR + 1][curC] != 0) {
                        curC --;
                        direction = 2;
                    }
                    else
                        curR ++;
                    break;
                case 2:
                    if (curC == 0 || result[curR][curC - 1] != 0) {
                        curR --;
                        direction = 3;
                    }
                    else
                        curC --;
                    break;
                case 3:
                    if (curR == 0 || result[curR - 1][curC] != 0) {
                        curC ++;
                        direction = 0;
                    }
                    else
                        curR --;
                    break;
            }
            count ++;
        }
        return result;
    }
};