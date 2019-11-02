// O(log(min(N+M))), by recursion
// https://leetcode.com/articles/median-of-two-sorted-arrays/#approach-1-recursive-approach-accepted
class Solution {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int m = nums1.size(), n = nums2.size();
		if (m > n) {
			swap(nums1, nums2);
			swap(m, n);
		}

		int iMin = 0, iMax = m;
		while (iMin <= iMax) {
			int i = (iMin + iMax) / 2;
			int j = (m + n + 1) / 2 - i;

			if (i < m && nums2[j - 1] > nums1[i]) // i is too small
				iMin = i + 1;
			else if (i > 0 && nums1[i - 1] > nums2[j]) // i is too large
				iMax = i - 1;
			else { // i is perfect!
				int maxLeft = 0, minRight = 0;
				if (i == 0)
					maxLeft = nums2[j - 1];
				else if (j == 0)
					maxLeft = nums1[i - 1];
				else
					maxLeft = max(nums1[i - 1], nums2[j - 1]);

				if (i == m)
					minRight = nums2[j];
				else if (j == n)
					minRight = nums1[i];
				else
					minRight = min(nums1[i], nums2[j]);

				return ((m + n) % 2 == 1) ? maxLeft : (maxLeft + minRight) / 2.0;
			}
		}
	}
};

// O((N+M)/2), merge two arrays
class Solution {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		int size = nums1.size() + nums2.size();
		int flag1 = 0, flag2 = 0, flag = 0;
		double median = 0;

		while (flag < size / 2 && flag1 < nums1.size() && flag2 < nums2.size()) {
			if (nums1[flag1] < nums2[flag2]) {
				median = nums1[flag1];
				flag1 ++;
			}
			else {
				median = nums2[flag2];
				flag2 ++;
			}
			flag ++;
		}

		if (flag1 == nums1.size()) {
			flag2 += (size / 2 - flag);
			if (size % 2 == 1)
				median = nums2[flag2];
			else {
				double temp;
				if (flag1 == 0)
					temp = nums2[flag2 - 1];
				else if (flag2 == 0)
					temp = nums1.back();
				else
					temp = max(nums1.back(), nums2[flag2 - 1]);
				median = ((double)nums2[flag2] + temp) / 2;
			}
		}
		else if (flag2 == nums2.size()) {
			flag1 += (size / 2 - flag);
			if (size % 2 == 1)
				median = nums1[flag1];
			else {
				double temp;
				if (flag2 == 0)
					temp = nums1[flag1 - 1];
				else if (flag1 == 0)
					temp = nums2.back();
				else
					temp = max(nums2.back(), nums1[flag1 - 1]);
				median = ((double)nums1[flag1] + temp) / 2;
			}
		}
		else {
			if (size % 2 == 1)
				median = min(nums1[flag1], nums2[flag2]);
			else
				median = ((double)median + min(nums1[flag1], nums2[flag2])) / 2;
		}		
		return median;
	}
};