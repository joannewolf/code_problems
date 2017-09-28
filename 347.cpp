#include <utility>
#include <algorithm>
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> counts;
        vector<vector<int>> buckets(nums.size(), vector<int>());
        vector<int> result;
        int flag = 0;

        for (int i : nums) {
        	if (counts.find(i) == counts.end())
        		counts[i] = 1;
        	else
        		counts[i] ++;
        }

        for (map<int, int>::iterator it = counts.begin(); it != counts.end(); it++)
        	buckets[(it -> second) - 1].push_back(it -> first);
        for (int i = buckets.size() - 1; i >= 0 && result.size() < k; i--)
        	result.insert(result.end(), buckets[i].begin(), buckets[i].end());

        return result;
    }
};