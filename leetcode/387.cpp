class Solution {
public:
    int firstUniqChar(string s) {
        if (s.length() == 0)
            return -1;
        string t(s), uniqueChar;
        sort(t.begin(), t.end());
        // get the set of unique char
        t.push_back('*');
        t.insert(t.begin(), '*');
        for (int i = 1; i < t.length() - 1; i++) {
            if (t[i] != t[i - 1] && t[i] != t[i + 1])
                uniqueChar.push_back(t[i]);
        }
        // find first unique char in original string
        int result = s.length();
        for (int i = 0; i < uniqueChar.length(); i++) {
            result = (s.find(uniqueChar[i]) < result) ? s.find(uniqueChar[i]) : result;
        }
        return (result == s.length()) ? -1 : result;
    }
};