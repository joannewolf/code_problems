#include <algorithm>
class Solution {
public:
    int maxCount(int m, int n, vector<vector<int>>& ops) {
        // get min(ops[i].a), means rows added by one the most time; same for min(ops[i].b)
        int minR = m, minC = n;
        for (int i = 0; i < ops.size(); i++) {
            minR = min(minR, ops[i][0]);
            minC = min(minC, ops[i][1]);
        }
        return (minR * minC);
    }
};