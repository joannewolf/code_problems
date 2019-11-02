class Solution {
public:
    string reverseStr(string s, int k) {
        int flag = 0;
        while (flag < s.length()) {
        	int reverseLength = (flag + k - 1 < s.length()) ? k : (s.length() - flag);
        	for (int i = 0; i < reverseLength / 2; i++) {
        		char temp = s[flag + i];
        		s[flag + i] = s[flag + reverseLength - 1 - i];
        		s[flag + reverseLength - 1 - i] = temp;
        	}
        	flag += (2 * k);
        }
        return s;
    }
};