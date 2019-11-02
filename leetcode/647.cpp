class Solution {
public:
    int countSubstrings(string s) {
        int result = 0, n = s.length();

        for (int i = 0; i < s.length(); i++) {
            // assume s[i] is center of odd palindrome
            int flag = 1;
            while ((i - flag) >= 0 && (i + flag) < n && s[i - flag] == s[i + flag]) {
                flag ++;
            }
            result += flag;

            // assume s[i] and s[i + 1] are center of even palindrome
            flag = 0;
            while ((i - flag) >= 0 && (i + flag + 1) < n && s[i - flag] == s[i + flag + 1]) {
                flag ++;
            }
            result += flag;
        }
        return result;
    }
};