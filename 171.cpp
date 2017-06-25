#include <math.h>
class Solution {
public:
    int titleToNumber(string s) {
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            result += pow(26, i) * (s[s.length() - 1 - i] - 64);
        }
        return result;
    }
};