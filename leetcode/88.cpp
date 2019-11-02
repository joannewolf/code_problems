class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if (m == 0) {
        	nums1 = nums2;
        	return;
        }

        vector<int> temp (nums1.begin(), nums1.begin() + m);
        nums1 = temp;
        vector<int> temp2 (nums2.begin(), nums2.begin() + n);
        nums2 = temp2;

        int flag1 = 0, flag2 = 0;
        while (flag2 < n) {
        	if (flag1 == nums1.size()) {
        		nums1.insert(nums1.end(), nums2[flag2]);
        		flag1 ++;
        		flag2 ++;
        	}
        	else if (nums2[flag2] <= nums1[flag1]) {
        		nums1.insert(nums1.begin() + flag1, nums2[flag2]);
        		flag1 ++;
        		flag2 ++;
        	}
        	else
        		flag1 ++;
        }
    }
};