#include <algorithm>
class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        if (timeSeries.size() == 0)
            return 0;
        int result = 0;
        for (int i = 1; i < timeSeries.size(); i++)
            result += min(timeSeries[i] - timeSeries[i - 1], duration);
        result += duration;
        return result;
    }
};