class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
        	return false;
        if (s.size() == t.size() && s.size() == 0)
        	return true;

       	sort(s.begin(), s.end());
       	sort(t.begin(), t.end());
       	return (s == t);
    }
};