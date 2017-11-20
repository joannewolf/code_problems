#include <utility>
#include <algorithm>
class Solution {
private:
    int quickSelect(vector<pair<int, int>>& counts, int start, int end, int target) {
        int l = start, r = end, pivot = counts[r].second;
        // partition the numbers into two groups: smaller than pivot, larger than pivot
        while (l < r) {
            if (counts[l].second > pivot) {
                r --;
                swap(counts[l], counts[r]);
            }
            else
                l ++;
        }
        swap(counts[l], counts[end]);

        if (l == target)
            return counts[l].second;
        else if (l < target) // target is in the right side of the pivot
            return quickSelect(counts, l + 1, end, target);
        else
            return quickSelect(counts, start, l - 1, target);
    }
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {  
        // count numbers
        map<int, int> counts;
        for (int i : nums) {
            if (counts.find(i) == counts.end())
                counts[i] = 1;
            else
                counts[i] ++;
        }

        // copy map into vector
        vector<pair<int, int>> countsVec;
        for (auto it = counts.begin(); it != counts.end(); it ++)
            countsVec.emplace_back(make_pair(it -> first, it -> second));

        // use quick selection to find the kth frequent element
        int kthElementCount = quickSelect(countsVec, 0, countsVec.size() - 1, countsVec.size() - k);

        // collect results which >= kth element count
        vector<int> result;
        for (int i = 0; i < countsVec.size() && result.size() < k; i++) {
            if (countsVec[i].second >= kthElementCount)
                result.emplace_back(countsVec[i].first);
        }
        
        return result;
    }
};