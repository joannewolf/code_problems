#include <math.h>
class Solution {
public:
    vector<int> constructRectangle(int area) {
        int length = sqrt(area);
        vector<int> result;
        while (area % length != 0)
            length ++;
        length = max(length, area / length);
        result.push_back(length);
        result.push_back(area / length);
        return result;
    }
};