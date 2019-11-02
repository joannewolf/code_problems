class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        if (nums.size() <= 1)
            return 0;
        int count = 0, first = 0, second = 1;
        sort(nums.begin(), nums.end());
        while (first < nums.size() && second < nums.size()) {
            if (nums[second] - nums[first] == k) {
                if ((first == 0 || nums[first] != nums[first - 1]) || (second == 1 || nums[second] != nums[second - 1]))
                    count ++;
                first ++;
                second ++;
            }
            else if (nums[second] - nums[first] < k)
                second ++;
            else {
                first ++;
                if (first == second)
                    second ++;
            }
        }

        return count;
    }
};