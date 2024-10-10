#include <stack>
class Solution {
public:
    bool isValid(string s) {
        stack<char> buf;
        for (int i = 0; i < s.length(); i++) {
        	if (s[i] == '(' || s[i] == '[' || s[i] == '{')
        		buf.push(s[i]);
        	else if (!buf.empty() && ((s[i] == ')' && buf.top() == '(') || (s[i] == ']' && buf.top() == '[') || (s[i] == '}' && buf.top() == '{')))
        		buf.pop();
        	else
        		return false;
        }
        return buf.empty();
    }
};