class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows <= 1)
            return s;
        vector<string> rows(numRows, "");
        int flag = 0, direction = 1;
        string result("");
        for (int i = 0; i < s.length(); i++) {
            rows[flag].push_back(s[i]);
            flag += direction;
            if (flag == numRows - 1)
                direction = -1;
            else if (flag == 0)
                direction = 1;
        }
        for (string s : rows)
            result += s;
        return result;
    }
};