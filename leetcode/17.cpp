#include <algorithm>
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.length() == 0 || find(digits.begin(), digits.end(), '0') != digits.end() || find(digits.begin(), digits.end(), '1') != digits.end())
        	return vector<string>();
        vector<string> letters(10, ""), result(1, "");
        letters[2] = "abc";
        letters[3] = "def";
        letters[4] = "ghi";
        letters[5] = "jkl";
        letters[6] = "mno";
        letters[7] = "pqrs";
        letters[8] = "tuv";
        letters[9] = "wxyz";
        for (int i = 0; i < digits.size(); i++) {
        	vector<string> temp;
			for (int j = 0; j < result.size(); j++) {
				string tempStr = result[j];
				for (int k = 0; k < letters[digits[i] - 48].length(); k++) {
					temp.push_back(tempStr + letters[digits[i] - 48][k]);
				}
			}
			result = temp;
        }
        return result;
    }
};