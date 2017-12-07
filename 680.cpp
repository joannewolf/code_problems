class Solution {
private:
	bool isPalindromeRange(string s, int start, int end) {
		while (start < end) {
			if (s[start] == s[end]) {
				start ++;
				end --;
			}
			else
				return false;
		}
		return true;
	}
public:
    bool validPalindrome(string s) {
    	int n = s.length();

        for (int i = 0; i < n / 2; i++) {
        	if (s[i] != s[n - i - 1]) {
        		return (isPalindromeRange(s, i + 1, n - i - 1) || isPalindromeRange(s, i, n - i - 2));
        	}
        }
        return true;
    }
};