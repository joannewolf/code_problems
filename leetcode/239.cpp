// O(N), use deque
class Solution {
public:
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<int>();

		vector<int> result;
		deque<int> window;

		for (int i = 0; i < k; i++) {
			while (!window.empty() && window.back() < nums[i])
				window.pop_back();
			window.emplace_back(nums[i]);
		}

		for (int i = k; i < nums.size(); i++) {
			result.emplace_back(window.front());

			if (nums[i - k] == window.front())
				window.pop_front();
			
			while (!window.empty() && window.back() < nums[i])
				window.pop_back();
			window.emplace_back(nums[i]);
		}
		result.emplace_back(window.front());

		return result;
	}
};

// O(N), two-pass
class Solution {
public:
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<int>();

		int n = nums.size();
		vector<int> result;
		vector<int> leftMax(n), rightMax(n);

		leftMax[0] = nums[0];
		rightMax[n - 1] = nums[n - 1];
		for (int i = 1; i < n; i++) {
			leftMax[i] = (i % k == 0) ? nums[i] : max(nums[i], leftMax[i - 1]);

			int j = n - i - 1;
			rightMax[j] = ((j + 1) % k == 0) ? nums[j] : max(nums[j], rightMax[j + 1]);
		}

		for (int i = 0; i <= n - k; i++) {
			result.emplace_back(max(rightMax[i], leftMax[i + k - 1]));
		}

		return result;
	}
};

// O(NKlogK), brute-force [TLE]
class Solution {
public:
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty())
			return vector<int>();

		vector<int> result, window(nums.begin(), nums.begin() + k);
		int n = nums.size();

		sort(window.begin(), window.end());
		result.emplace_back(window.back());

		for (int i = k; i < n; i++) {
			// update window
			window.erase(find(window.begin(), window.end(), nums[i - k]));
			window.emplace_back(nums[i]);

			// find current maximum
			sort(window.begin(), window.end());
			result.emplace_back(window.back());			
		}

		return result;
	}
};