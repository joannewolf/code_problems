// O(NlogK), use multiset and update middle iterator
class Solution {
public:
	vector<double> medianSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<double>();

		int n = nums.size();
		vector<double> result;
		multiset<int> window(nums.begin(), nums.begin() + k);

		nums.emplace_back(INT_MIN);

		auto middle = next(window.begin(), k / 2);
		for (int i = k; i <= n; i++) {
			result.emplace_back(((double)*middle + *prev(middle, 1 - k % 2)) / 2);
			window.insert(nums[i]);
			if (nums[i] < *middle) // in C++11, newly inserted elements follow their equivalents already in the container
				middle --;

			if (nums[i - k] <= *middle)
				middle ++;
			window.erase(window.find(nums[i - k])); // erase the first element with value nums[i - k]
		}

		return result;
	}
};

// O(NlogK), use two heaps
class Solution {
public:
	vector<double> medianSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<double>();

		int n = nums.size();
		vector<double> result;
		unordered_map<int, int> toBeRemoved;
		priority_queue<int> leftHalf; // max heap, for numbers <= current median
		priority_queue<int, vector<int>, greater<int>> rightHalf; // min heap, for numbers >= current median

  		// initial window
		for (int i = 0; i < k; i++)
			leftHalf.emplace(nums[i]);
		for (int i = 0; i < k / 2; i++) {
			rightHalf.emplace(leftHalf.top());
			leftHalf.pop();
		}

		nums.emplace_back(INT_MIN);
		for (int i = k; i <= n; i++) {
			result.emplace_back((k % 2 == 1) ? leftHalf.top() : ((double)leftHalf.top() + rightHalf.top()) / 2);

			// remove nums[i - k]
			int balance = (nums[i - k] <= leftHalf.top()) ? -1 : 1;
			toBeRemoved[nums[i - k]] ++;
			
			// insert nums[i]
			if (!leftHalf.empty() && nums[i] <= leftHalf.top()) {
				balance ++;
				leftHalf.emplace(nums[i]);
			}
			else {
				balance --;
				rightHalf.emplace(nums[i]);
			}

			// re-balance two heaps
			if (balance < 0) {
				leftHalf.emplace(rightHalf.top());
				rightHalf.pop();
			}
			else if (balance > 0) {
				rightHalf.emplace(leftHalf.top());
				leftHalf.pop();
			}

			while (!leftHalf.empty() && toBeRemoved[leftHalf.top()]) {
				toBeRemoved[leftHalf.top()] --;
				leftHalf.pop();
			}
			while (!rightHalf.empty() && toBeRemoved[rightHalf.top()]) {
				toBeRemoved[rightHalf.top()] --;
				rightHalf.pop();
			}
		}

		return result;
	}
};

// O(NlogK), same algorithm as above, use multiset instead to easily implement
class Solution {
public:
	vector<double> medianSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<double>();

		int n = nums.size();
		vector<double> result;
		multiset<int> leftHalf, rightHalf;

  		// initial window
		for (int i = 0; i < k; i++)
			leftHalf.emplace(nums[i]);
		for (int i = 0; i < k / 2; i++) {
			rightHalf.emplace(*leftHalf.rbegin());
			leftHalf.erase(prev(leftHalf.end()));
		}

		nums.emplace_back(INT_MIN);
		for (int i = k; i <= n; i++) {
			result.emplace_back((k % 2 == 1) ? *leftHalf.rbegin() : ((double)*leftHalf.rbegin() + *rightHalf.begin()) / 2);

			// remove nums[i - k]
			int balance = 0;
			if (nums[i - k] <= *leftHalf.rbegin()) {
				balance --;
				leftHalf.erase(leftHalf.find(nums[i - k]));
			}
			else {
				balance ++;
				rightHalf.erase(rightHalf.find(nums[i - k]));
			}
			
			// insert nums[i]
			if (!leftHalf.empty() && nums[i] <= *leftHalf.rbegin()) {
				balance ++;
				leftHalf.insert(nums[i]);
			}
			else {
				balance --;
				rightHalf.insert(nums[i]);
			}

			// re-balance two heaps
			if (balance < 0) {
				leftHalf.insert(*rightHalf.begin());
				rightHalf.erase(rightHalf.begin());
			}
			else if (balance > 0) {
				rightHalf.insert(*leftHalf.rbegin());
				leftHalf.erase(prev(leftHalf.end()));
			}
		}

		return result;
	}
};

// O(NlogK), use deque
class Solution {
public:
	vector<double> medianSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<double>();

		int n = nums.size();
		vector<double> result;
		deque<int> window(nums.begin(), nums.begin() + k);

		nums.emplace_back(INT_MIN);

		int middleIndex = k / 2;
		for (int i = k; i <= n; i++) {
			vector<int> temp(window.begin(), window.end());
			if (k % 2 == 1) {
				nth_element(temp.begin(), temp.begin() + middleIndex, temp.end());
				result.emplace_back(temp[middleIndex]);
			}
			else {
				nth_element(temp.begin(), temp.begin() + middleIndex, temp.end());
				result.emplace_back(temp[middleIndex]);
				nth_element(temp.begin(), temp.begin() + middleIndex - 1, temp.end());
				result.back() = (result.back() + temp[middleIndex - 1]) / 2;
			}

			window.pop_front();
			window.emplace_back(nums[i]);
		}

		return result;
	}
};

// O(NKlogK), brute-force [TLE]
class Solution {
public:
	vector<double> medianSlidingWindow(vector<int>& nums, int k) {
		if (nums.empty() || k <= 0)
			return vector<double>();

		int n = nums.size();
		vector<double> result;
		vector<int> window(nums.begin(), nums.begin() + k);

		nums.emplace_back(INT_MIN);

		int middleIndex = k / 2;
		for (int i = k; i <= n; i++) {
			sort(window.begin(), window.end());
			if (k % 2 == 1)
				result.emplace_back(window[middleIndex]);
			else
				result.emplace_back(((double)window[middleIndex - 1] + window[middleIndex]) / 2);

			window.erase(find(window.begin(), window.end(), nums[i - k]));
			window.emplace_back(nums[i]);
		}

		return result;
	}
};