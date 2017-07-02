class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        string row1 = "qwertyuiopQWERTYUIOP", row2 = "asdfghjklASDFGHJKL", row3 = "zxcvbnmZXCVBNM";
        for (int i = 0; i < words.size(); i++) {
            if (words[i].length() == 0)
                continue;
            bool inRow1 = true, inRow2 = true, inRow3 = true;
            for (int j = 0; j < words[i].length(); j++) {
                if (row1.find(words[i][j]) == -1) {
                    inRow1 = false;
                    break;
                }
            }
            for (int j = 0; j < words[i].length(); j++) {
                if (row2.find(words[i][j]) == -1) {
                    inRow2 = false;
                    break;
                }
            }
            for (int j = 0; j < words[i].length(); j++) {
                if (row3.find(words[i][j]) == -1) {
                    inRow3 = false;
                    break;
                }
            }
            if (!inRow1 && !inRow2 && !inRow3) {
                words.erase(words.begin() + i);
                i --;
            }
        }
        return words;
    }
};