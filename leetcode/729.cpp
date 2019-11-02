// O(N), search ranges linearly
class MyCalendar {
private:
	vector<pair<int, int>> calendars;
public:
	MyCalendar() {}
	
	bool book(int start, int end) {
		for (pair<int, int> calendar : calendars) {
			if ((calendar.first <= start && start < calendar.second) || 
				(calendar.first < end && end <= calendar.second) || 
				(start < calendar.first && calendar.second < end))
				return false;
		}
		calendars.emplace_back(make_pair(start, end));
		return true;
	}
};

// O(logN), maintain sorted ranges and use binary search
class MyCalendar {
private:
	vector<pair<int, int>> calendars;
public:
	MyCalendar() {}
	
	bool book(int start, int end) {
		int l = 0, r = calendars.size() - 1;
		while (l <= r) {
			int middle = (l + r) / 2;
			if (calendars[middle].first == start)
				return false;
			else if (calendars[middle].first < start)
				l = middle + 1;
			else
				r = middle - 1;
		}
		if ((l != calendars.size() && calendars[l].first < end) || 
			(l != 0 && start < calendars[l - 1].second))
			return false;

		calendars.insert(calendars.begin() + l, make_pair(start, end));
		return true;
	}
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.book(start,end);
 */