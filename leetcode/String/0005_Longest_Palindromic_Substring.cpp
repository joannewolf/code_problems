class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length() == 0)
            return "";
        string result;

        for (int i = 0; i < s.length(); i++) {
            // assume s[i] is center of odd palindrome
            int flag = 1;
            while ((i - flag) >= 0 && (i + flag) < s.length() && s[i - flag] == s[i + flag]) {
                flag ++;
            }
            if ((flag - 1) * 2 + 1 > result.length())
                result = s.substr(i - flag + 1, (flag - 1) * 2 + 1);
            // assume s[i] and s[i + 1] are center of even palindrome
            flag = 1;
            if (i != s.length() - 1 && s[i] == s[i + 1]) {
                while ((i - flag) >= 0 && (i + flag + 1) < s.length() && s[i - flag] == s[i + flag + 1]) {
                    flag ++;
                }
                if ((flag - 1) * 2 + 2 > result.length())
                    result = s.substr(i - flag + 1, (flag - 1) * 2 + 2);
            }
        }
        return result;
    }
};