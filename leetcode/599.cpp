#include <map>
#include <climits>
class Solution {
public:
    vector<string> findRestaurant(vector<string>& list1, vector<string>& list2) {
        map<string, int> m;
        int minIndexSum = INT_MAX;
        vector<string> result;
        for (int i = 0; i < list1.size(); i++)
            m[list1[i]] = i;
        for (int i = 0; i < list2.size(); i++) {
            if (m.find(list2[i]) == m.end())
                continue;
            if (m[list2[i]] + i < minIndexSum) {
                minIndexSum = m[list2[i]] + i;
                result.clear();
                result.push_back(list2[i]);
            }
            else if (m[list2[i]] + i == minIndexSum)
                result.push_back(list2[i]);
        }
        return result;
    }
};