class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        if (target == 0) {
            result.push_back(vector<int>());
            return result;
        }
        if (candidates.size() == 0 || target < 0)
            return result;

        sort(candidates.begin(), candidates.end());
        if (target < candidates[0])
            return result;

        for (int i = candidates.size() - 1; i >= 0; i--) {
            if (target == candidates[i]) {
                result.push_back(vector<int>(1, candidates[i]));
            }
            else if (target > candidates[i]) {
                vector<int> newCandidates(candidates.begin(), candidates.begin() + i + 1);
                vector<vector<int>> temp = combinationSum(newCandidates, target - candidates[i]);
                for (vector<int> v : temp) {
                    v.push_back(candidates[i]);
                    result.push_back(v);
                }
            }
        }

        return result;
    }
};