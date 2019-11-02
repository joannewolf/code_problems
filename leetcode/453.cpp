#include <algorithm>
class Solution {
public:
    int minMoves(vector<int>& nums) {
        // plus n - 1 elements by 1 == minus 1 element by 1
        vector<int>::iterator minNumPos = min_element(nums.begin(), nums.end());
        int minNum = nums[minNumPos - nums.begin()], result = 0;
        for (int i = 0; i < nums.size(); i++)
            result += (nums[i] - minNum);
        return result;
    }
};