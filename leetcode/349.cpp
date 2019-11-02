class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> result;
        if (nums1.size() == 0 || nums2.size() == 0)
        	return result;
        
        int flag1 = 0, flag2 = 0;
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        while (flag1 < nums1.size() && flag2 < nums2.size()) {
        	if ((flag1 != 0 && nums1[flag1] == nums1[flag1 - 1]) || (nums1[flag1] < nums2[flag2]))
        		flag1 ++;
        	else if ((flag2 != 0 && nums2[flag2] == nums2[flag2 - 1]) || (nums1[flag1] > nums2[flag2]))
        		flag2 ++;
        	else if (nums1[flag1] == nums2[flag2]) {
        		result.push_back(nums1[flag1]);
        		flag1 ++;
        		flag2 ++;
        	}
        }

        return result;
    }
};