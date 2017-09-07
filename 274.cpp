#include <algorithm>
class Solution {
public:
    int hIndex(vector<int>& citations) {
        if (citations.size() == 0)
        	return 0;

        int n = citations.size(), result = 0;
        sort(citations.begin(), citations.end());
        for (int i = 0; i < n; i++)
        	result = max(result, min(citations[i], n - i));
        return result;
    }
};