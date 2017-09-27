#include <algorithm>
class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
    	int n = nums.size();
    	// store Max(player1 score - player2 score) for subarray [i, j]
    	vector<int> current(n, 0), previous(n, 0);

    	previous[n - 1] = nums[n - 1];

    	for (int i = n - 2; i >= 0; i--) {
    		current[i] = nums[i];
    		for (int j = i + 1; j < n; j++)
    			current[j] = max(nums[i] - previous[j], nums[j] - current[j - 1]);
    		previous = current;
    	}

    	return (current.back() >= 0);
    }
};