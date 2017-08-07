#include <utility>
class Solution {
public:
    int triangleNumber(vector<int>& nums) {
        if (nums.size() < 3)
            return 0;
        int result = 0;
        vector<pair<int, int>> count;
        // count all numbers
        sort(nums.begin(), nums.end());
        for (int i : nums) {
            if (i <= 0)
                continue;
            if (count.empty() || count.back().first != i)
                count.push_back(make_pair(i, 1));
            else
                count.back().second ++;
        }

        for (int i = 0; i < count.size(); i++) {
            // regular triangle
            if (count[i].second >= 3)
                result += (count[i].second * (count[i].second - 1) * (count[i].second - 2) / 6);

            // isosceles triangle
            if (count[i].second >= 2) {
                for (int j = 0; j < i; j++)
                    result += ((count[i].second) * (count[i].second - 1) / 2 * (count[j].second));
                for (int j = i + 1; j < count.size(); j++) {
                    if (count[i].first * 2 > count[j].first)
                        result += ((count[i].second) * (count[i].second - 1) / 2 * (count[j].second));
                    else
                        break;
                }
            }

            // triangle
            for (int j = i + 1; j < count.size(); j++) {
                for (int k = j + 1; k < count.size(); k++) {
                    if (count[i].first + count[j].first > count[k].first)
                        result += (count[i].second * count[j].second * count[k].second);
                    else
                        break;
                }
            }
        }

        return result;
    }
};