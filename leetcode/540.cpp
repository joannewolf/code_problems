// O(logN), O(1) space
class Solution {
public:
	int singleNonDuplicate(vector<int>& nums) {
		int n = nums.size(), l = 0, r = n / 2;
		while (l < r) {
			int mid = (l + r) / 2;
			if (nums[2 * mid] != nums[2 * mid + 1])
				r = mid;
			else
				l = mid + 1;
		}
		return nums[2 * l];
	}
};

// O(logN), O(1) space
class Solution {
public:
	int singleNonDuplicate(vector<int>& nums) {
		int l = 0, r = nums.size() - 1;
		while (l < r) {
			int mid = (l + r) / 2;
			// always get the left element in the pair, or the single element
			if (mid % 2 == 1)
				mid --;

			if (nums[mid] != nums[mid + 1])
				r = mid;
			else
				l = mid + 2;
		}
		return nums[l];
	}
};


// O(logN), O(1) space
class Solution {
public:
	int singleNonDuplicate(vector<int>& nums) {
		if (nums.size() == 1)
			return nums[0];

		int l = 0, r = nums.size() - 1, n = nums.size();
		while (n > 3) {
			int mid = (l + r) / 2;
			if (nums[mid] != nums[mid - 1] && nums[mid] != nums[mid + 1])
				return nums[mid];

			if (n % 4 == 3) {
				if (nums[mid] == nums[mid - 1])
					l = mid + 1;
				else
					r = mid - 1;
				n -= (n / 2 + 1);
			}
			else if (n % 4 == 1) {
				if (nums[mid] == nums[mid - 1])
					r = mid;
				else
					l = mid;
				n -= (n / 2);
			}
		}
		return (nums[l] != nums[l + 1]) ? nums[l] : nums[r];
	}
};