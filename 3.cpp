class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string tempStr = "";
        int maxLength = 0;
        for (int i = 0; i < s.length(); i++) {
            int temp = tempStr.find(s[i]);
            if (temp == -1)
                tempStr.push_back(s[i]);
            else {
                maxLength = max(maxLength, (int)(tempStr.length()));
                tempStr = tempStr.substr(temp + 1);
                tempStr.push_back(s[i]);
            }
        }

        return max(maxLength, (int)(tempStr.length()));
    }
};