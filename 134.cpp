class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        vector<int> nums;
        int n = gas.size(), minNum = 0, minFlag;

        for (int i = 0; i < n; i++) {
        	nums.push_back(gas[i] - cost[i]);
        	if (nums.back() <= minNum) {
        		minNum = nums.back();
        		minFlag = i;
        	}
        }

        for (int i = 0; i < n; i++) {
        	bool complete = false;
        	int temp = 0;
        	for (int j = 0; j < n; j++) {
        		temp += nums[(i + minFlag + 1 + j) % n];
        		if (temp < 0)
        			break;
        		if (j == n - 1)
        			return ((i + minFlag + 1) % n);
        	}
        }
        return -1;
    }
};