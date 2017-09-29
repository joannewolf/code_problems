class Solution {
public:
    void reverseWords(string &s) {
        vector<string> words(1, "");
        for (char c : s) {
        	if (c == ' ' && words.back().length() != 0)
       			words.push_back("");
       		else if (c != ' ')
       			words.back().push_back(c);
        }
        s.clear();
        if (words.back().empty())
        	words.pop_back();
        for (int i = words.size() - 1; i >= 0; i--)
        	s += (words[i] + " ");
        s.pop_back();
    }
};