// simulation
class Solution {
private:
	set<int> digits;
	bool isValid(int hour, int minute) {
		return (digits.find(hour / 10) != digits.end()) && (digits.find(hour % 10) != digits.end()) && 
			(digits.find(minute / 10) != digits.end()) && (digits.find(minute % 10) != digits.end());
	}
public:
	string nextClosestTime(string time) {
		// collect all useful digits
		for (char c : time) {
			if (isdigit(c))
				digits.insert(c - '0');
		}

		// foward the time one second at a time
		int hour = stoi(time.substr(0, 2));
		int minute = stoi(time.substr(3, 2));
		for (int i = 0; i < 24 * 60; i++) {
			minute += 1;
			if (minute == 60) {
				minute = 0;
				hour += 1;
			}
			if (hour == 24)
				hour = 0;

			if (isValid(hour, minute)) {
				char result[5];
				sprintf(result, "%02d:%02d", hour, minute);
				return string(result);
			}
		}
	}
};

// build from allowed digits, by iteration
class Solution {
public:
	string nextClosestTime(string time) {
		// collect all useful digits
		set<char> digits;
		for (char c : time) {
			if (isdigit(c))
				digits.insert(c);
		}

		// find all possible time
		vector<string> times, validTimes;
		times.emplace_back("");
		for (int i = 0; i < 4; i++) {
			vector<string> clone(times), newTimes;
			for (string str : clone) {
				for (char c : digits) {
					newTimes.emplace_back(str + c);
				}
			}
			times = newTimes;
		}

		// choose valid time
		for (string str : times) {
			if (stoi(str.substr(0, 2)) <= 23 && stoi(str.substr(2)) <= 59)
				validTimes.emplace_back(str);
		}

		// return the next closet one
		string target = time;
		target.erase(2, 1);
		int flag = find(validTimes.begin(), validTimes.end(), target) - validTimes.begin();
		string result = validTimes[(flag + 1) % validTimes.size()];
		result.insert(2, ":");
		return result;
	}
};

// build from allowed digits, by dfs recursion
class Solution {
private:
	set<char> digits;
	void dfs(int index, string &temp, vector<string> &times) {
		if (index == 5) {
			if (stoi(temp.substr(0, 2)) <= 23 && stoi(temp.substr(3, 2)) <= 59)
				times.emplace_back(temp);
		}
		else {
			for (char c : digits) {
				temp[index] = c;
				if (index == 1)
					dfs(3, temp, times);
				else
					dfs(index + 1, temp, times);
			}
		}
	}
public:
	string nextClosestTime(string time) {
		// collect all useful digits
		for (char c : time) {
			if (isdigit(c))
				digits.insert(c);
		}

		// find all valid time
		string temp = "  :  ";
		vector<string> times;
		dfs(0, temp, times);

		// return the next closet one
		int flag = find(times.begin(), times.end(), time) - times.begin();
		return times[(flag + 1) % times.size()];
	}
};