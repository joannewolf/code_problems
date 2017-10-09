class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> result, checked(nums.size() + 1, 0);
        for (int i : nums) {
        	if (checked[i] != 0)
        		result.push_back(i);
        	checked[i] ++;
        }

        return result;
    }
};