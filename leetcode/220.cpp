// O(N^2), brute-force
class Solution {
public:
	bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
		for (int i = 0; i < nums.size(); i++) {
			for (int j = 1; j <= k && i + j < nums.size(); j++) {
				if (abs((long long)nums[i] - nums[i + j]) <= (long long)t)
					return true;
			}
		}
		return false;
	}
};

// O(NlogK), maintain a window with size k and use binary search to find the nearest value
class Solution {
public:
	bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
		if (nums.size() == 0 || k <= 0)
			return false;

		set<int> window;
		for (int i = 0; i < nums.size(); i++) {
			auto it = window.lower_bound(nums[i]);
			if (it != window.end() && *it - (long long)nums[i] <= (long long)t)
				return true;
			if (it != window.begin() && (long long)nums[i] - *(--it) <= (long long)t)
				return true;

			window.insert(nums[i]);
			if (i >= k)
				window.erase(nums[i - k]);
		}
		return false;
	}
};

// O(N), use buckets with size t + 1, and maintain the previous k elements
// the almost duplicate numbers may be in same bucket or in neighbor buckets
class Solution {
private:
	long long getBucketId(long long i, long long w) {
		return i < 0 ? (i + 1) / w - 1 : i / w;
	}
public:
	bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
		if (nums.size() < 2 || k <= 0 || t < 0)
			return false;

		unordered_map<long long, long long> buckets;
		long long windowSize = t + 1;
		for (int i = 0; i < nums.size(); i++) {
			long long bucketId = getBucketId(nums[i], windowSize);
			if (buckets.find(bucketId) != buckets.end() ||
				(buckets.find(bucketId - 1) != buckets.end() && nums[i] - buckets[bucketId - 1] <= t) ||
				(buckets.find(bucketId + 1) != buckets.end() && buckets[bucketId + 1] - nums[i] <= t))
				return true;

			buckets[bucketId] = nums[i];
			if (i >= k)
				buckets.erase(getBucketId(nums[i - k], windowSize));
		}
		return false;
	}
};