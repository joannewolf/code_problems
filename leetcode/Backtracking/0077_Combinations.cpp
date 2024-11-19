class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        if (n < 1 || k < 0)
            return vector<vector<int>>();
        if (k == 0)
            return vector<vector<int>>(1, vector<int>());
        
        vector<vector<int>> result;
        if (k == 1) {
            for (int i = 1; i <= n; i++)
                result.push_back(vector<int>(1, i));
        }
        else {
            for (int i = n; i > 1; i--) {
                vector<vector<int>> temp = combine(i - 1, k - 1);
                for (vector<int> v : temp) {
                    v.push_back(i);
                    result.push_back(v);
                }
            }
        }
        return result;
    }
};