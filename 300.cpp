// O(NlogN), binary search
class Solution {
public:
	int lengthOfLIS(vector<int>& nums) {
		if (nums.size() == 0)
			return 0;
		
		vector<int> IS;
		IS.push_back(nums[0]);
		for (int i = 1; i < nums.size(); i++) {
			// find nums[i] should be inserted in which position in increasing subsequence
			int l = 0, r = IS.size() - 1;
			while (l <= r) {
				int mid = (l + r) / 2;
				if (IS[mid] < nums[i])
					l = mid + 1;
				else
					r = mid - 1;
			}
			if (l < IS.size())
				IS[l] = nums[i];
			else
				IS.push_back(nums[i]);
		}
		return IS.size();
	}
};

// O(N^2), dynamic programming
class Solution {
public:
	int lengthOfLIS(vector<int>& nums) {
		if (nums.size() == 0)
			return 0;
		
		int n = nums.size(), maxLength = 1;
		vector<int> ISlength(n, 1);
		// ISlength[i]: the max length of increasing subsequence until nums[i]

		for (int i = 1; i < n; i++) {
			for (int j = i - 1; j >= 0; j--) {
				if (nums[i] > nums[j])
					ISlength[i] = max(ISlength[i], ISlength[j] + 1);
			}
			maxLength = max(maxLength, ISlength[i]);
		}
		return maxLength;
	}
};