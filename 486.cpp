#include <utility>
class Solution {
private:
	pair<int, int> calculateScores(vector<int> nums) {
		if (nums.size() == 1)
			return make_pair(nums[0], 0);
		if (nums.size() == 2)
			return (nums[0] >= nums[1]) ? make_pair(nums[0], nums[1]) : make_pair(nums[1], nums[0]);
		pair<int, int> score1 = calculateScores(vector<int>(nums.begin() + 1, nums.end()));
		pair<int, int> score2 = calculateScores(vector<int>(nums.begin(), nums.end() - 1));
		return (nums[0] + score1.second >= nums.back() + score2.second) ? make_pair(nums[0] + score1.second, score1.first) : make_pair(nums.back() + score2.second, score2.first);
	}
public:
    bool PredictTheWinner(vector<int>& nums) {
        pair<int, int> scores = calculateScores(nums);
        return (scores.first >= scores.second);
    }
};