class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() == 0) {
            result.push_back(vector<int>());
            return result;
        }
        if (nums.size() == 1) {
            result.push_back(vector<int>(nums));
            return result;
        }

        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i != 0 && nums[i] == nums[i - 1])
                continue;
            vector<int> newNums(nums);
            newNums.erase(newNums.begin() + i);
            vector<vector<int>> temp = permuteUnique(newNums);
            for (vector<int> v : temp) {
                v.push_back(nums[i]);
                result.push_back(v);
            }
        }
        return result;
    }
};