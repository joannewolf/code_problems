class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<bool> appeared(nums.size() + 1, false);
        vector<int> result;
        for (int i = 0; i < nums.size(); i++)
            appeared[nums[i]] = true;
        for (int i = 1; i < appeared.size(); i++) {
            if (!appeared[i])
                result.push_back(i);
        }
        return result;
    }
};