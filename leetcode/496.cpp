#include <stack>
#include <algorithm>
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        stack<int> s;
        vector<int> greater(nums.size(), -1), result;
        for (int i = 0; i < nums.size(); i++) {
            while (!s.empty() && nums[i] > nums[s.top()]) {
                greater[s.top()] = nums[i];
                s.pop();
            }
            s.push(i);
        }
        for (int i = 0; i < findNums.size(); i++) {
            result.push_back(greater[ find(nums.begin(), nums.end(), findNums[i]) - nums.begin() ]);
        }
        return result;
    }
};