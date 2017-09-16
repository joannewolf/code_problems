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