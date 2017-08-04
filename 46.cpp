class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        if (nums.size() == 0) {
            result.push_back(vector<int>());
            return result;
        }
        if (nums.size() == 1) {
            result.push_back(nums);
            return result;
        }
        for (int i = 0; i < nums.size(); i++) {
            vector<int> newNums(nums);
            newNums.erase(newNums.begin() + i);
            vector<vector<int>> temp = permute(newNums);
            for (vector<int> t : temp) {
                t.push_back(nums[i]);
                result.push_back(t);
            }
        }
        return result;
    }
};