#include <ctype.h>
class Solution {
public:
    bool isPalindrome(string s) {
        // remove all space and lower all alphabets
        for (int i = 0; i < s.length(); i++) {
            if (!isalnum(s[i])) {
                s.erase(s.begin() + i);
                i --;
            }
            else if (isupper(s[i]))
                s[i] = tolower(s[i]);
        }
        // determine if palindrome
        for (int i = 0; i < s.length() / 2; i++) {
            if (s[i] != s[s.length() - 1 - i])
                return false;
        }
        return true;
    }
};