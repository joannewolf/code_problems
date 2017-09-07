#include <algorithm>
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size(), result = 0;
        for (int i = 0; i < n; i++) {
        	if (min(citations[i], n - i) >= result)
        		result = min(citations[i], n - i);
        	else
        		return result;
        }
        return result;
    }
};