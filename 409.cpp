#include <algorithm>
class Solution {
public:
    int longestPalindrome(string s) {
        if (s.length() == 0)
            return 0;
        sort(s.begin(), s.end());
        int result = 0, oddExist = 0;
        vector<int> count;
        // count the number of letters
        count.push_back(1);
        for (int i = 1; i < s.length(); i++) {
            if (s[i] == s[i - 1])
                count.back() ++;
            else
                count.push_back(1);
        }
        // add all even numbers and maximum odd number
        for (int i = 0; i < count.size(); i++) {
            if (count[i] % 2 == 0)
                result += count[i];
            else {
                oddExist = 1;
                result += (count[i] - 1);
            }
        }
        result += oddExist;
        return result;
    }
};