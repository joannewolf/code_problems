#include <algorithm>
/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
class Solution {
private:
    static bool mySortInterval (Interval first, Interval second) {
        return (first.start < second.start); 
    }
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        if (intervals.size() == 0)
            return intervals;
        sort(intervals.begin(), intervals.end(), mySortInterval);
        for (int i = 0; i < intervals.size() - 1; i++) {
            if (intervals[i].end >= intervals[i + 1].start) {
                intervals[i].end = max(intervals[i].end, intervals[i + 1].end);
                intervals.erase(intervals.begin() + i + 1);
                i --;
            }
        }
        return intervals;
    }
};