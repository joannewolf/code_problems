class Solution {
public:
    int findLHS(vector<int>& nums) {
        map<int, int> count;
        int result = 0, lastNum = 0, lastCount = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (count.find(nums[i]) == count.end())
                count[nums[i]] = 1;
            else
                count[nums[i]] ++;
        }

        for (pair<int, int> p : count) {
            if (lastCount != 0 && p.first == lastNum + 1 && p.second + lastCount > result)
                result = p.second + lastCount;
            lastNum = p.first;
            lastCount = p.second;
        }

        return result;
    }
};