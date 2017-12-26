// O(N)
class Solution {
public:
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		int n = gas.size(), l = 0, r = n - 1, sum = 0;

		while (l < r) {
			if (sum + gas[l] - cost[l] >= 0) {
				sum += (gas[l] - cost[l]);
				l ++;
			}
			else {
				sum += (gas[r] - cost[r]);
				r --;
			}
		}
		return (sum + gas[l] - cost[l] >= 0) ? (l + 1) % n : -1;
	}
};

// O(N)
// If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)
// If the total number of gas is bigger than the total number of cost. There must be a solution.
class Solution {
public:
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		int start = 0, total = 0, tank = 0;
		for (int i = 0; i < gas.size(); i++) {
			tank += (gas[i] - cost[i]);
			if (tank < 0) {
				start = i + 1;
				total += tank;
				tank = 0;
			}
		}
		return (total + tank < 0) ? -1 : start;
	}
};

// O(N^2)
class Solution {
public:
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
		vector<int> nums;
		int n = gas.size();

		for (int i = 0; i < n; i++)
			nums.push_back(gas[i] - cost[i]);

		// try every starting index
		for (int i = 0; i < n; i++) {
			int temp = 0;
			for (int j = 0; j < n; j++) {
				temp += nums[(i + j) % n];
				if (temp < 0)
					break;
				if (j == n - 1)
					return i;
			}
		}
		return -1;
	}
};