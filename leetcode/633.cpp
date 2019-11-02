#include <vector>
class Solution {
public:
    bool judgeSquareSum(int c) {
        if (c < 0)
            return false;
        // 46340^2 < INT_MAX
        int l = 0, r = 46340;
        while (l <= r) {
            if (l * l + r * r == c)
                return true;
            else if (l * l + r * r < c)
                l ++;
            else
                r --;
        }

        return false;
    }
};