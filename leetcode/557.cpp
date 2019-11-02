class Solution {
public:
    string reverseWords(string s) {
        int flag = 0, count = 0;
        while (flag < s.length()) {
        	int wordLength = (s.substr(flag).find(' ') != -1) ? s.substr(flag).find(' ') : (s.length() - flag);
        	for (int i = 0; i < wordLength / 2; i++) {
        		char temp = s[flag + i];
        		s[flag + i] = s[flag + wordLength - 1 - i];
        		s[flag + wordLength - 1 - i] = temp;
        	}
        	flag += (wordLength + 1);
        }
        return s;
    }
};