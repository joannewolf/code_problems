#include <algorithm>
class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        int result = 0, flag1 = 0, flag2 = 0;
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        // for each house, find the nearest heater
        while (flag1 < houses.size() && flag2 < heaters.size()) {
            if (houses[flag1] > heaters[flag2])
                flag2 ++;
            else if (houses[flag1] < heaters[flag2]) {
                int distance = (flag2 != 0) ? min(heaters[flag2] - houses[flag1], houses[flag1] - heaters[flag2 - 1]) : heaters[flag2] - houses[flag1];
                result = (distance > result) ? distance : result;
                flag1 ++;
            }
            else {
                flag1 ++;
                flag2 ++;
            }
        }
        if (houses.back() - heaters.back() > result)
            result = houses.back() - heaters.back();
        return result;
    }
};