#include <algorithm>
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        if (triangle.size() == 0)
        	return 0;
        if (triangle.size() == 1)
        	return triangle[0][0];

        int n = triangle.size();
        vector<int> previous_sum = triangle[0], current_sum;
        for (int i = 1; i < n; i++) {
        	current_sum.push_back(triangle[i][0] + previous_sum[0]);
        	for (int j = 1; j < i; j++) {
        		current_sum.push_back(triangle[i][j] + min(previous_sum[j - 1], previous_sum[j]));
        	}
        	current_sum.push_back(triangle[i].back() + previous_sum.back());
        	previous_sum = current_sum;
        	current_sum.clear();
        }
        vector<int>::iterator it = min_element(previous_sum.begin(), previous_sum.end());
        return *it;
    }
};