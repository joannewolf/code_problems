#include <math.h>
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        result.push_back(0);
        for (int i = 0; i < n; i++) {
            int sz = result.size();
            for (int j = sz - 1; j >= 0; j--)
                result.push_back(result[j] + pow(2, i));
        }
        return result;
    }
};