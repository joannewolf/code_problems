// O(N), bucket sort
class Solution {
public:
	int hIndex(vector<int>& citations) {
		int n = citations.size();
		vector<int> buckets(n + 1, 0);

		for (int i : citations) {
			if (i >= n)
				buckets[n] ++;
			else
				buckets[i] ++;
		}

		int count = 0;
		for (int i = n; i >= 0; i--) {
			count += buckets[i];
			if (count >= i)
				return i;
		}
		return 0;
	}
};


// O(NlogN + logN)
class Solution {
public:
	int hIndex(vector<int>& citations) {
		if (citations.size() == 0)
			return 0;

		// find the minimum index such that citations[index] >= citations.size() - index, result = citations.size() - index
		sort(citations.begin(), citations.end());
		int n = citations.size(), l = 0, r = n - 1;

		while (l <= r) {
			int mid = (l + r) / 2;
			if (citations[mid] < n - mid)
				l = mid + 1;
			else
				r = mid - 1;
		}
		return (n - l);
	}
};

// O(NlogN + N)
class Solution {
public:
	int hIndex(vector<int>& citations) {
		if (citations.size() == 0)
			return 0;

		int n = citations.size(), result = 0;
		sort(citations.begin(), citations.end());
		for (int i = 0; i < n; i++)
			result = max(result, min(citations[i], n - i));
		return result;
	}
};