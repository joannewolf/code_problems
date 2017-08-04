class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
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
            if (i != candidates.size() - 1 && candidates[i] == candidates[i + 1])
                continue;
            if (target >= candidates[i]) {
                vector<int> newCandidates(candidates.begin(), candidates.begin() + i);
                vector<vector<int>> temp = combinationSum2(newCandidates, target - candidates[i]);
                for (vector<int> v : temp) {
                    v.push_back(candidates[i]);
                    result.push_back(v);
                }
            }
        }

        return result;
    }
};