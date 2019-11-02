class Solution {
private:
	bool isPalindrome(string s) {
		int n = s.length();
		for (int i = 0; i < n / 2; i++) {
			if (s[i] != s[n - i - 1])
				return false;
		}
		return true;
	}
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        if (s.empty()) {
        	result.push_back(vector<string>());
        	return result;
        }

        int n = s.length();
        for (int i = 1; i <= n; i++) {
        	vector<vector<string>> tempResult;
        	if (isPalindrome(s.substr(0, i)))
        		tempResult = partition(s.substr(i));
        	for (vector<string> &strs : tempResult) 
        		strs.insert(strs.begin(), s.substr(0, i));
        	result.insert(result.end(), tempResult.begin(), tempResult.end());
        }
        return result;
    }
};