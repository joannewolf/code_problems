class Solution {
public:
    int numDecodings(string s) {
    	if (s.length() == 0 || s[0] == '0')
    		return 0;
    	if (s.length() == 1)
    		return 1;

        vector<int> count(s.length(), 0);
        count[0] = 1;
        for (int i = 1; i < s.length(); i++) {
        	if (s[i] == '0') {
        		if (s[i - 1] >= '3' || s[i - 1] == '0')
        			return 0;
        		else
        			count[i] = (i == 1) ? 1 : count[i - 2];
        	}
        	else {
	        	count[i] = count[i - 1];
	        	if (s[i - 1] == '1' || (s[i - 1] == '2' && s[i] <= '6'))
	        		count[i] += ((i == 1) ? 1 : count[i - 2]);
        	}
        }
        return count.back();
    }
};