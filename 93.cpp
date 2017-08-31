#include <string>
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        vector<string> result;
        if (s.length() < 4 || s.length() > 12)
        	return result;

        for (int i = 1; i <= 3; i ++) {
        	int temp = s.length() - i;
        	if (temp < 3 || temp > 9 || stoi(s.substr(0, i)) > 255 || (s[0] == '0' && i != 1))
        		continue;
        	for (int j = 1; j <= 3; j ++) {
        		int temp2 = s.length() - i - j;
        		if (temp2 < 2 || temp2 > 6 || stoi(s.substr(i, j)) > 255 || (s[i] == '0' && j != 1))
        			continue;
        		for (int k = 1; k <= 3; k++) {
        			int temp3 = s.length() - i - j - k;
	        		if (temp3 < 1 || temp3 > 3 || stoi(s.substr(i + j, k)) > 255 || (s[i + j] == '0' && k != 1) || stoi(s.substr(i + j + k)) > 255 || (s[i + j + k] == '0' && temp3 != 1))
	        			continue;
	        		string str = s.substr(0, i) + "." + s.substr(i, j) + "." + s.substr(i + j, k) + "." + s.substr(i + j + k);
	        		result.push_back(str);
        		}
        	}
        }
        return result;
    }
};