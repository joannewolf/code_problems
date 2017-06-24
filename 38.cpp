class Solution {
public:
    string countAndSay(int n) {
        string result = "1";
        
        for (int i = 1; i < n; i++) {
        	string temp;
        	int count = 1;
        	for (int j = 1; j < result.length(); j++) {
        		if (result[j] == result[j - 1])
        			count ++;
        		else {
        			temp.push_back(count + 48);
        			temp.push_back(result[j - 1]);
        			count = 1;
        		}
        	}
        	temp.push_back(count + 48);
        	temp.push_back(result.back());
        	result = temp;
        }

        return result;
    }
};