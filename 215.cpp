// O(N) in avg, quick selection
class Solution {
private:
	void swap(vector<int>& nums, int index1, int index2) {
		int temp = nums[index1];
		nums[index1] = nums[index2];
		nums[index2] = temp;
	}

	int quickSelect(vector<int>& nums, int start, int end, int target) {
		int l = start, r = end, pivot = nums[r];
		// partition the numbers into two groups: smaller than pivot, larger than pivot
		while (l < r) {
			if (nums[l] > pivot) {
				r --;
				swap(nums, l, r);
			}
			else
				l ++;
		}
		swap(nums, l, end);

		if (l == target)
			return nums[l];
		else if (l < target) // target is in the right side of the pivot
			return quickSelect(nums, l + 1, end, target);
		else
			return quickSelect(nums, start, l - 1, target);
	}
public:
	int findKthLargest(vector<int>& nums, int k) {
		if (nums.size() == 0 || k <= 0 || nums.size() < k)
			return -1;
		return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
	}
};

// O(NlogK), use priority queue
class Solution {
public:
	int findKthLargest(vector<int>& nums, int k) {
		priority_queue<int, vector<int>, greater<int>> pq;
		for (int i : nums) {
			pq.push(i);
			if (pq.size() > k)
				pq.pop();
		}
		return pq.top();
	}
};

// O(NlogN)
class Solution {
public:
	int findKthLargest(vector<int>& nums, int k) {
		sort(nums.begin(), nums.end());
		return nums[nums.size() - k];
	}
};