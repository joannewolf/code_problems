#include <vector>
#include <string>
#include <algorithm>
using namespace std;
class Solution {
public:
    int findSubstringInWraproundString(string p) {
        if (p.length() == 0)
            return 0;
        
        vector<int> vec(26, 0);
        // vec[i] means the maximum length of substring starting with ith letter
        // e.g. vec[2] = 3 means c, cd, cde these 3 substrings are included in the result.
        p = p + '-'; // append a fake end char
        char flag = p[0];
        int substrLen = 1;
        for (int i = 1; i < p.length(); i++) {
            if ((p[i] == p[i - 1] + 1) || (p[i] == 'a' && p[i - 1] == 'z'))
                substrLen ++;
            else {
                char temp = flag;
                for (int j = 0; j < max(26, substrLen); j++) {
                    if (vec[temp - 'a'] < substrLen - j)
                        vec[temp - 'a'] = substrLen - j;
                    temp = (temp != 'z') ? temp + 1 : 'a';
                }
                flag = p[i];
                substrLen = 1;
            }
        }

        int result = 0;
        for (int i = 0; i < 26; i++) {
            result += vec[i];
        }
        return result;
    }
};