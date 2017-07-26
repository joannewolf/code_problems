class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1, rotate;
        // find index of smallest value, same as the rotate pivot
        while (l < r) {
        	int middle = (l + r) / 2;
        	if (nums[middle] > nums[r])
        		l = middle + 1;
        	else
        		r = middle;
        }
        rotate = l;
        printf("rotate %d\n", rotate);

        // find index of target
        l = 0, r = nums.size() - 1;
        while (l <= r) {
        	int middle = (l + r) / 2;
        	int realMiddle = (middle + rotate) % nums.size();
        	if (nums[realMiddle] == target)
        		return realMiddle;
        	else if (nums[realMiddle] < target)
        		l = middle + 1;
        	else
        		r = middle - 1;
        }

        return -1;
    }
};