#include <utility>
#include <algorithm>

class mycomparison{
private:
	vector<int> nums1;
	vector<int> nums2;
public:
	mycomparison(vector<int> &n1, vector<int> &n2) {
		this -> nums1 = n1;
		this -> nums2 = n2;
	}
	bool operator() (const pair<int, int>& p1, const pair<int, int>& p2) {
		return (nums1[p1.first] + nums2[p1.second] > nums1[p2.first] + nums2[p2.second]);
	}
};

class Solution {
public:
    vector<pair<int, int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<pair<int, int>> result;
        if (nums1.size() == 0 || nums2.size() == 0 || k == 0)
        	return result;

        priority_queue<pair<int, int>, vector<pair<int, int>>, mycomparison> pq(mycomparison(nums1, nums2));
        int n = min(k, (int)nums1.size() * (int)nums2.size());

        for (int i = 0; i < min(k, (int)nums1.size()); i++)
        	pq.emplace(make_pair(i, 0));

        for (int i = 0; i < n; i++) {
        	pair<int, int> next = pq.top();
        	pq.pop();
        	result.emplace_back(make_pair(nums1[next.first], nums2[next.second]));
        	if (next.second < nums2.size() - 1)
        		pq.emplace(make_pair(next.first, next.second + 1));
        }

        return result;
    }
};