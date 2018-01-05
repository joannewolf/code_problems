class RangeModule {
private:
	vector<pair<int, int>> ranges;

public:
	RangeModule() {
	}
	
	void addRange(int left, int right) {
		int leftRange = getBoundRanges(left);
		int rightRange = getBoundRanges(right);

		if (leftRange == rightRange && (rightRange == ranges.size() || right < ranges[rightRange].first))
			ranges.insert(ranges.begin() + leftRange, make_pair(left, right));
		else {
			if (rightRange == ranges.size() || right < ranges[rightRange].first)
				rightRange --;
			ranges[leftRange].first = min(ranges[leftRange].first, left);
			ranges[leftRange].second = max(ranges[rightRange].second, right);
			ranges.erase(ranges.begin() + leftRange + 1, ranges.begin() + rightRange + 1);
		}
		// printRanges();
	}
	
	void removeRange(int left, int right) {
		int leftRange = getBoundRanges(left);
		int rightRange = getBoundRanges(right);

		if (leftRange == rightRange && leftRange != ranges.size() && ranges[leftRange].first < left && right < ranges[rightRange].second) {
			ranges.insert(ranges.begin() + leftRange, make_pair(ranges[leftRange].first, left));
			ranges[leftRange + 1].first = right;
		}
		else {
			if (leftRange != ranges.size() && ranges[leftRange].first < left) {
				ranges[leftRange].second = min(ranges[leftRange].second, left);
				leftRange ++;
			}
			if ((rightRange != ranges.size() && right < ranges[rightRange].second)) {
				ranges[rightRange].first = max(ranges[rightRange].first, right);
				rightRange --;
			}

			if (rightRange == ranges.size())
				rightRange --;

			if (leftRange <= rightRange && left <= ranges[leftRange].first && ranges[rightRange].second <= right)
				ranges.erase(ranges.begin() + leftRange, ranges.begin() + rightRange + 1);
		}
		// printRanges();
	}

	bool queryRange(int left, int right) {
		for (int i = 0; i < ranges.size(); i++) {
			if (ranges[i].first <= left && right <= ranges[i].second)
				return true;
		}
		return false;
	}

	void printRanges() {
		for (int i = 0; i < ranges.size(); i++)
			printf("[%d, %d] ", ranges[i].first, ranges[i].second);
		cout << endl;
	}

	int getBoundRanges(int index) {
		int rangeIndex = -1;
		int l = 0, r = ranges.size() - 1;

		while (l <= r) {
			int mid = (l + r) / 2;
			if (ranges[mid].first <= index && index <= ranges[mid].second) {
				rangeIndex = mid;
				break;
			}
			else if (ranges[mid].second < index)
				l = mid + 1;
			else if (index < ranges[mid].first)
				r = mid - 1;
		}
		if (rangeIndex == -1)
			rangeIndex = l;

		// cout << "index " << index << " range " << rangeIndex << endl;
		return rangeIndex;
	}

};

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * bool param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */