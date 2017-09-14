class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        stack<int> st;
        int n = s.length();
        vector<int> checked(n, false);

        st.push(0);
        while (!st.empty()) {
        	int temp = st.top();
        	st.pop();
        	if (temp == n)
        		return true;
        	else if (temp > n || checked[temp])
        		continue;

        	for (string word : wordDict) {
        		if (s.substr(temp, word.length()) == word) {
        			checked[temp] = true;
        			st.push(temp + word.length());
        		}
        	}
        }

        return false;
    }
};

