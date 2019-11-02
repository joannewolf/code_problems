#include <utility>
class Solution {
private:
    static bool mysort(pair<int, int> a, pair<int, int> b) {
        return (a.first > b.first);
    }
public:
    vector<string> findRelativeRanks(vector<int>& nums) {
        vector<string> result (nums.size(), "");
        if (nums.size() == 0)
            return result;

        vector<pair<int, int>> index;
        for (int i = 0; i < nums.size(); i++)
            index.push_back(make_pair(nums[i], i));
        sort(index.begin(), index.end(), mysort);

        for (int i = 0; i < index.size(); i++) {
            if (i == 0)
                result[index[0].second] = "Gold Medal";
            else if (i == 1)
                result[index[1].second] = "Silver Medal";
            else if (i == 2)
                result[index[2].second] = "Bronze Medal";
            else
                result[index[i].second] = to_string(i + 1);
        }
        return result;
    }
};