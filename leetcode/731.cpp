// O(N), search range linearly
class MyCalendarTwo {
private:
	vector<pair<int, int>> calendars1, calendars2;
public:
	MyCalendarTwo() {}
	
	bool book(int start, int end) {
		for (pair<int, int> &calendar : calendars2) {
			if (calendar.first < end && start < calendar.second)
				return false;
		}
		for (pair<int, int> &calendar : calendars1) {
			if (calendar.first < end && start < calendar.second)
				calendars2.emplace_back(make_pair(max(start, calendar.first), min(end, calendar.second)));
		}
		calendars1.emplace_back(make_pair(start, end));
		return true;
	}
};

// O(N), count boundary
class MyCalendarTwo {
private:
	map<int, int> count;
public:
	MyCalendarTwo() {}
	
	bool book(int start, int end) {
		if (count.find(start) == count.end())
			count[start] = 1;
		else
			count[start] ++;
		if (count.find(end) == count.end())
			count[end] = -1;
		else
			count[end] --;

		int active = 0;
		for (auto it = count.begin(); it != count.end(); it ++) {
			active += (it -> second);
			if (active >= 3) {
				// undo
				if (count[start] == 1)
					count.erase(start);
				else
					count[start] --;
				if (count[end] == -1)
					count.erase(end);
				else
					count[end] ++;
				return false;
			}
		}
		return true;
	}
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * bool param_1 = obj.book(start,end);
 */