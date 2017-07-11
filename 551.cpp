class Solution {
public:
    bool checkRecord(string s) {
        int countA = 0, countL = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'A') {
                countA ++;
                if (countA > 1)
                    return false;
            }
            if (s[i] == 'L') {
                if (countL == 1 && s[i - 1] == 'L')
                    countL ++;
                else if (countL == 2 && s[i - 1] == 'L' && s[i - 2] == 'L')
                    return false;
                else
                    countL = 1;
            }
        }
        return true;
    }
};