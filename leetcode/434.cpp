class Solution {
public:
    int countSegments(string s) {
        if (s.length() == 0)
            return 0;
        int count = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s[i] == ' ' && s[i - 1] != ' ')
                count ++;
        }
        if (s.back() != ' ')
            count ++;
        return count;
    }
};