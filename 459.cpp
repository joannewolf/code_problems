#include <vector>
#include <math.h>
class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        if (s.length() <= 1)
            return false;

        vector<int> factors;
        int str_length = s.length();

        // add all factors of length of string
        factors.push_back(1);
        for (int i = 2; i <= sqrt(str_length); i++) {
            if (str_length % i == 0) {
                factors.push_back(i);
                if (str_length / i != i)
                    factors.push_back(str_length / i);
            }
        }

        // check all possible substrings
        for (int i = 0; i < factors.size(); i++) {
            bool isRepeated = true;
            string pattern = s.substr(0, factors[i]);
            for (int j = factors[i]; j < s.length(); j += factors[i]) {
                if (s.substr(j, factors[i]) != pattern) {
                    isRepeated = false;
                    break;
                }
            }
            if (isRepeated)
                return true;
        }
        return false;
    }
};