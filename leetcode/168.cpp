#include <string>
class Solution {
public:
    string convertToTitle(int n) {
        string result;
        while (n != 0) {
            if (n % 26 == 0) {
                result.insert(result.begin(), 'Z');
                n -= 26;
            }
            else
                result.insert(result.begin(), (n % 26) + 64);
            n /= 26;
        }
        return result;
    }
};