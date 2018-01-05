// sumRange & update O(sqrt(N)), O(sqrt(N)) space for sqrt(N) buckets
class NumArray {
private:
	int k, m;
	// m buckets, k elements per bucket
	vector<vector<int>> buckets;
	vector<int> bucketSums;
public:
	NumArray(vector<int> nums) {
		int n = nums.size();
		if (n == 0)
			return;
		k = sqrt(n);
		m = n / k + 1;
		buckets = vector<vector<int>>(m, vector<int>(k));
		for (int i = 0; i < m; i++) {
			int sum = 0;
			for (int j = 0; j < k && i * k + j < n; j++) {
				buckets[i][j] = nums[i * k + j];
				sum += nums[i * k + j];
			}
			bucketSums.emplace_back(sum);
		}
	}
	
	void update(int i, int val) {
		bucketSums[i / k] = bucketSums[i / k] - buckets[i / k][i % k] + val;
		buckets[i / k][i % k] = val;
	}
	
	int sumRange(int i, int j) {
		int sum = 0;
		if (i / k == j / k) {
			for (int x = i % k; x <= j % k; x++)
				sum += buckets[i / k][x];
		}
		else {
			for (int x = i % k; x < k; x++)
				sum += buckets[i / k][x];
			for (int x = i / k + 1; x < j / k; x++)
				sum += bucketSums[x];
			for (int x = 0; x <= j % k; x++)
				sum += buckets[j / k][x];
		}
		return sum;
	}
};

// sumRange & update O(logN), construct segment tree O(N), O(N) space
// use segment tree to record the sum of subarrays, and implement with array
class NumArray {
private:
	vector<int> segTree;
	int n;
public:
	NumArray(vector<int> nums) {
		n = nums.size();
		segTree = vector<int>(2 * n, 0);

		// build tree
		for (int i = n, j = 0; i < 2 * n; i++, j++)
			segTree[i] = nums[j];
		for (int i = n - 1; i > 0; i--)
			segTree[i] = segTree[2 * i] + segTree[2 * i + 1];
	}
	
	void update(int i, int val) {
		i += n;
		segTree[i] = val;
		while (i > 0) {
			if (i % 2 == 0)
			// it's left child of its parent
				segTree[i / 2] = segTree[i] + segTree[i + 1];
			else
			// it's right child of its parent
				segTree[i / 2] = segTree[i - 1] + segTree[i];
			i /= 2;
		}
	}
	
	int sumRange(int i, int j) {
		int result = 0;
		i += n;
		j += n;
		while (i <= j) {
			if (i % 2 == 1) {
				result += segTree[i];
				i++;
			}
			if (j % 2 == 0) {
				result += segTree[j];
				j--;
			}
			i /= 2;
			j /= 2;
		}
		return result;
	}
};

// sumRange & update O(logN), construct segment tree O(NlogN), O(N) space
// use binary indexed tree
// https://discuss.leetcode.com/topic/31599/java-using-binary-indexed-tree-with-clear-explanation
class NumArray {
private:
	vector<int> BIT;
	vector<int> nums;
	int n;

	void init(int i, int val) {
		i++;
		while (i <= n) {
			BIT[i] += val;
			i += (i & -i);
		}
	}

	int getSum(int i) {
		int result = 0;
		i++;
		while (i > 0) {
			result += BIT[i];
			i -= (i & -i);
		}
		return result;
	}
public:
	NumArray(vector<int> nums) {
		n = nums.size();
		BIT = vector<int>(n + 1, 0);
		this -> nums = nums;
		for (int i = 0; i < n; i++)
			init(i, nums[i]);
	}
	
	void update(int i, int val) {
		int diff = val - nums[i];
		nums[i] = val;
		init(i, diff);
	}
	
	int sumRange(int i, int j) {
		return getSum(j) - getSum(i - 1);
	}
};