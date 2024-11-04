#include <stack>
class Solution {
public:
    string decodeString(string s) {
        string numStr;
        stack<string> strStack;
        stack<int> countStack;

        strStack.emplace("");
        countStack.emplace(1);

        for (char c : s) {
            if (isdigit(c)) {
                numStr += c;
            }
            else if (c == '[') {
                countStack.emplace(stoi(numStr));
                numStr.clear();
                strStack.emplace("");
            }
            else if (c == ']') {
                int count = countStack.top();
                string str = strStack.top();
                countStack.pop();
                strStack.pop();
                for (int i = 0; i < count; i++)
                    strStack.top() += str;
            }
            else {
                strStack.top() += c;
            }
        }

        return strStack.top();
    }
};