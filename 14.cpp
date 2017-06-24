class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    	if (strs.size() == 0)
    		return "";

    	string prefix = "";
    	int flag = 0;
    	while (1) {
    		for (int i = 0; i < strs.size(); i++) {
	    		if (flag > strs[i].length() || strs[i][flag] != strs[0][flag])
	    			return prefix;
	    	}
	    	prefix.push_back(strs[0][flag]);
	    	flag ++;
    	}
    	
    	return prefix;
    }
};