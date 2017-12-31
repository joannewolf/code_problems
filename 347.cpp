// O(N) in avg., quick selection
class Solution {
private:
	int quickSelect(vector<pair<int, int>>& counts, int start, int end, int target) {
		int l = start, r = end, pivot = counts[r].second;
		// partition the numbers into two groups: smaller than pivot, larger than pivot
		while (l < r) {
			if (counts[l].second > pivot) {
				r --;
				swap(counts[l], counts[r]);
			}
			else
				l ++;
		}
		swap(counts[l], counts[end]);

		if (l == target)
			return counts[l].second;
		else if (l < target) // target is in the right side of the pivot
			return quickSelect(counts, l + 1, end, target);
		else
			return quickSelect(counts, start, l - 1, target);
	}
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {  
		// count numbers
		map<int, int> counts;
		for (int i : nums) {
			if (counts.find(i) == counts.end())
				counts[i] = 1;
			else
				counts[i] ++;
		}

		// copy map into vector
		vector<pair<int, int>> countsVec;
		for (auto it = counts.begin(); it != counts.end(); it ++)
			countsVec.emplace_back(make_pair(it -> first, it -> second));

		// use quick selection to find the kth frequent element
		int kthElementCount = quickSelect(countsVec, 0, countsVec.size() - 1, countsVec.size() - k);

		// collect results which >= kth element count
		vector<int> result;
		for (int i = 0; i < countsVec.size() && result.size() < k; i++) {
			if (countsVec[i].second >= kthElementCount)
				result.emplace_back(countsVec[i].first);
		}
		
		return result;
	}
};

// O(N), bucket sort
class Solution {
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {
		map<int, int> counts;
		vector<vector<int>> buckets(nums.size(), vector<int>());
		vector<int> result;
		int flag = 0;

		for (int i : nums) {
			if (counts.find(i) == counts.end())
				counts[i] = 1;
			else
				counts[i] ++;
		}

		for (map<int, int>::iterator it = counts.begin(); it != counts.end(); it++)
			buckets[(it -> second) - 1].push_back(it -> first);
		for (int i = buckets.size() - 1; i >= 0 && result.size() < k; i--)
			result.insert(result.end(), buckets[i].begin(), buckets[i].end());

		return result;
	}
};

// O(NlogK), use heap
class Solution {
private:
	static bool compareCounts(const pair<int, int> a, const pair<int, int> b) {
		return (a.second != b.second) ? (a.second > b.second) : (a.first > b.first);
	}
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {
		map<int, int> counts;
		for (int i : nums) {
			if (counts.find(i) == counts.end())
				counts[i] = 1;
			else
				counts[i] ++;
		}

		priority_queue<pair<int, int>, vector<pair<int, int>>, function<bool(pair<int, int>, pair<int, int>)>> pq(compareCounts);
		for (auto it = counts.begin(); it != counts.end(); it++) {
			pq.emplace(make_pair(it -> first, it -> second));
			if (pq.size() > k)
				pq.pop();
		}

		vector<int> result(k);
		for (int i = 0; i < k; i++) {
			result[i] = pq.top().first;
			pq.pop();
		}
		return result;
	}
};

// O(NlogN)
class Solution {
private:
	static bool compareCounts(const pair<int, int> a, const pair<int, int> b) {
		return (a.second != b.second) ? (a.second > b.second) : (a.first > b.first);
	}
public:
	vector<int> topKFrequent(vector<int>& nums, int k) {
		map<int, int> counts;
		vector<pair<int, int>> countsVec;
		vector<int> result;

		for (int i : nums) {
			if (counts.find(i) == counts.end())
				counts[i] = 1;
			else
				counts[i] ++;
		}
		for (map<int, int>::iterator it = counts.begin(); it != counts.end(); it++)
			countsVec.push_back(make_pair(it -> first, it -> second));
		sort(countsVec.begin(), countsVec.end(), compareCounts);
		for (int i = 0; i < k; i++)
			result.push_back(countsVec[i].first);
		return result;
	}
};
