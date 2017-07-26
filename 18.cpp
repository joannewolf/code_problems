class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        if (nums.size() < 4)
            return result;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 3; i++) {
            if (i != 0 && nums[i] == nums[i - 1])
                continue;
            for (int j = i + 1; j < nums.size() - 2; j++) {
                if (j != i + 1 && nums[j] == nums[j - 1])
                    continue;
                int l = j + 1, r = nums.size() - 1;
                while (l < r) {
                    if (l != j + 1 && nums[l] == nums[l - 1]) {
                        l ++;
                        continue;
                    }
                    if (r != nums.size() - 1 && nums[r] == nums[r + 1]) {
                        r --;
                        continue;
                    }
                    int temp = nums[i] + nums[j] + nums[l] + nums[r];
                    if (temp == target) {
                        vector<int> quadruplet;
                        quadruplet.push_back(nums[i]);
                        quadruplet.push_back(nums[j]);
                        quadruplet.push_back(nums[l]);
                        quadruplet.push_back(nums[r]);
                        result.push_back(quadruplet);
                        l ++;
                        r --;
                    }
                    else if (temp < target)
                        l ++;
                    else
                        r --;
                }
            }
        }
        return result;
    }
};