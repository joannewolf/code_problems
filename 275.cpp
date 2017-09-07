#include <algorithm>
class Solution {
public:
    int hIndex(vector<int>& citations) {
    	// find the minimum index such that citations[index] >= citations.size() - index, result = citations.size() - index
        int n = citations.size(), l = 0, r = n - 1;

        while (l <= r) {
        	int mid = (l + r) / 2;
        	if (citations[mid] < n - mid)
        		l = mid + 1;
        	else
        		r = mid - 1;
        }
        return (n - l);
    }
};