#include <utility>
#include <algorithm>
class Solution {
private:
	static bool compareCounts(const pair<int, int> a, const pair<int, int> b) {
		return (a.second != b.second) ? (a.second > b.second) : (a.first > b.first);
	}
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counts;
        vector<pair<int, int>> countsVec;
        vector<int> result;

        for (int i : nums) {
        	if (counts.find(i) == counts.end())
        		counts[i] = 1;
        	else
        		counts[i] ++;
        }
        for (map<int, int>::iterator it = counts.begin(); it != counts.end(); it++)
        	countsVec.push_back(make_pair(it -> first, it -> second));
        sort(countsVec.begin(), countsVec.end(), compareCounts);
        for (int i = 0; i < k; i++)
        	result.push_back(countsVec[i].first);
        return result;
    }
};