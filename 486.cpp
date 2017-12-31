// O(N^2), dynamic programming, O(N) space
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

// O(N^2), dynamic programming, O(N^2) space
class Solution {
public:
    bool PredictTheWinner(vector<int>& nums) {
        int n = nums.size();
        // store Max(player1 score - player2 score) for subarray [i, j]
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++)
            dp[i][i] = nums[i];
        for (int i = n - 2; i >= 0; i--) {
            for (int j = i + 1; j < n; j++)
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }

        return (dp[0][n - 1] >= 0);
    }
};

// O(2^N), by recursion
class Solution {
private:
    pair<int, int> calculateScores(vector<int> nums) {
        if (nums.size() == 1)
            return make_pair(nums[0], 0);
        if (nums.size() == 2)
            return (nums[0] >= nums[1]) ? make_pair(nums[0], nums[1]) : make_pair(nums[1], nums[0]);
        pair<int, int> score1 = calculateScores(vector<int>(nums.begin() + 1, nums.end()));
        pair<int, int> score2 = calculateScores(vector<int>(nums.begin(), nums.end() - 1));
        return (nums.front() + score1.second >= nums.back() + score2.second) ? make_pair(nums.front() + score1.second, score1.first) : make_pair(nums.back() + score2.second, score2.first);
    }
public:
    bool PredictTheWinner(vector<int>& nums) {
        pair<int, int> scores = calculateScores(nums);
        return (scores.first >= scores.second);
    }
};