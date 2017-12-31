// sumRange O(sqrt(N)), O(sqrt(N)) space for sqrt(N) buckets
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