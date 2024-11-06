#include <utility>
#include <climits>
class Solution {
private:
	static bool sortPoints(pair<int, int> a, pair<int, int> b) {
		return (a.second != b.second) ? (a.second < b.second) : (a.first < b.first);
	}
public:
    int findMinArrowShots(vector<pair<int, int>>& points) {
        if (points.size() == 0)
        	return 0;
        
        int result = 1, n = points.size();
        sort(points.begin(), points.end(), sortPoints);
        int arrow = points[0].second;

        for (int i = 1; i < n; i++) {
        	if (points[i].first > arrow) {
        		arrow = points[i].second;
        		result ++;
        	}
        }
        return result;
    }
};