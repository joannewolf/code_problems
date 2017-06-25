class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        if (numRows >= 1) {
        	vector<int> temp (1, 1);
        	result.push_back(temp);
        }
        for (int i = 2; i <= numRows; i++) {
        	vector<int> temp;
        	temp.push_back(1);
        	for (int j = 0; j < result.back().size() - 1; j++)
        		temp.push_back(result.back()[j] + result.back()[j + 1]);
        	temp.push_back(1);
        	result.push_back(temp);
        }

        return result;
    }
};