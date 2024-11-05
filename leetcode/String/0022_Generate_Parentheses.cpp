class Solution {
private:
	vector<string> genParenthesis(int usedLeft, int usedRight, int n) {
		vector<string> result;
		if (usedLeft == n && usedRight == n) {
			result.push_back("");
		}
		if (usedLeft < n) {
			vector<string> temp = genParenthesis(usedLeft + 1, usedRight, n);
			for (string s : temp)
				result.push_back("(" + s);
		}
		if (usedRight + 1 <= usedLeft) {
			vector<string> temp = genParenthesis(usedLeft, usedRight + 1, n);
			for (string s : temp)
				result.push_back(")" + s);
		}
		return result;
	}
public:
    vector<string> generateParenthesis(int n) {
        return genParenthesis(0, 0, n);
    }
};