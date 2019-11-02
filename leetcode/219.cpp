// O(N), use map to record index
class Solution {
public:
	bool containsNearbyDuplicate(vector<int>& nums, int k) {
		if (k <= 0)
			return false;

		map<int, int> pos;
		for(int i = 0; i < nums.size(); i++) {
			if (pos.find(nums[i]) != pos.end() && i - pos[nums[i]] <= k)
				// appeared, compare the distance
				return true;
			else
				// add new entry in map, or update the index
				pos[nums[i]] = i;
		}
		return false;
	}
};

// O(N), use set to record window with size k
class Solution {
public:
	bool containsNearbyDuplicate(vector<int>& nums, int k) {
		unordered_set<int> set;
		for (int i = 0; i < nums.size(); i++) {
			if (set.find(nums[i]) != set.end())
				return true;

			set.insert(nums[i]);
			if (i >= k)
				set.erase(nums[i - k]);
		}
		return false;
	}
};