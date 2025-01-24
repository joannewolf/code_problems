class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int S) {
    	map<int, int> sums;
    	sums[0] = 1;

        for (int i : nums) {
        	map<int, int> temp;
        	for (auto s : sums) {
        		if (temp.find(s.first + i) == temp.end())
        			temp[s.first + i] = s.second;
        		else
        			temp[s.first + i] += s.second;
        		if (temp.find(s.first - i) == temp.end())
        			temp[s.first - i] = s.second;
        		else
        			temp[s.first - i] += s.second;
        	}
        	sums = temp;
        }

        return (sums.find(S) != sums.end()) ? sums[S] : 0;
    }
};