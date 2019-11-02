// O(logN)
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;

        while (l < r) {
        	if (nums[l] < nums[r])
        		return nums[l];

        	int middle = (l + r) / 2;
        	if (nums[l] <= nums[middle])
        		l = middle + 1;
        	else
        		r = middle;
        }
        return nums[l];
    }
};

// O(N)
class Solution {
public:
    int findMin(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 1; i++) {
            if (nums[i] > nums[i + 1])
                return nums[i + 1];
        }
        return nums[0];
    }
};