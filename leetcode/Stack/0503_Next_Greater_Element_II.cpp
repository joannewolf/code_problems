class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int flag = 0, n = nums.size();
        stack<int> s;
        vector<int> greater(n, -1);
        for (int i = 0; i < n; i++) {
            while (!s.empty() && nums[i] > nums[s.top()]) {
                greater[s.top()] = nums[i];
                s.pop();
            }
            s.push(i);
            if (i == n - 1 && flag == 0) {
            	flag ++;
            	i = -1;
            }
        }
        return greater;
    }
};