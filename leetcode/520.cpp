#include <ctype.h>
class Solution {
public:
    bool detectCapitalUse(string word) {
        if (word.length() <= 1)
            return true;

        if (islower(word[0])) {
            // type 1: all letters are not capital
            for (int i = 1; i < word.length(); i++) {
                if (!islower(word[i]))
                    return false;
            }
        }
        else if (isupper(word[1])){
            // type 2: all letters are capital
            for (int i = 2; i < word.length(); i++) {
                if (!isupper(word[i]))
                    return false;
            }
        }
        else {
            // type 3: only first letter is capital
            for (int i = 2; i < word.length(); i++) {
                if (!islower(word[i]))
                    return false;
            }
        }
        return true;
    }
};