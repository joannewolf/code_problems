class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        if (nums.size() == 0 || nums[0].size() == 0 || r <= 0 || c <= 0 || nums.size() * nums[0].size() != r * c)
            return nums;

        vector<vector<int>> newMatrix;
        int flagR = 0, flagC = 0;
        for (int i = 0; i < r; i++) {
            vector<int> temp;
            for (int j = 0; j < c; j++) {
                temp.push_back(nums[flagR][flagC]);
                if (flagC == nums[0].size() - 1) {
                    flagC = 0;
                    flagR ++;
                }
                else
                    flagC ++;
            }
            newMatrix.push_back(temp);
        }

        return newMatrix;
    }
};