#include <algorithm>
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        for (int i = 1; i < s.length(); i++) {
            // has appeared in s but different in t OR not appeared in s but appeared in t
            if ((s.find(s[i]) < i && t[s.find(s[i])] != t[i]) || (s.find(s[i]) == i && t.find(t[i]) < i))
                return false;
        }
        return true;
    }
};