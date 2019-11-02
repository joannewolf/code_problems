class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    	vector<int> result;
    	if (nums1.size() == 0 || nums2.size() == 0)
    		return result;

    	int flag1 = 0, flag2 = 0;
    	sort(nums1.begin(), nums1.end());
    	sort(nums2.begin(), nums2.end());
    	while (flag1 < nums1.size() && flag2 < nums2.size()) {
    		if (nums1[flag1] < nums2[flag2])
    			flag1 ++;
    		else if (nums1[flag1] > nums2[flag2])
    			flag2 ++;
    		else {
    			result.push_back(nums1[flag1]);
    			flag1 ++;
    			flag2 ++;
    		}
    	}   
    	return result;
    }
};