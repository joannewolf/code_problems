class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount == 0)
        	return 0;
        if (coins.size() == 0 || amount < 0)
        	return -1;

        vector<int> combinations(amount + 1, -1);
        combinations[0] = 0;
		for (int i = 1; i <= amount; i++) {
			int temp = INT_MAX;
			for (int c : coins) {
				if (i - c >= 0 && combinations[i - c] != -1 && combinations[i - c] < temp)
					temp = combinations[i - c];
			}
			combinations[i] = (temp != INT_MAX) ? (temp + 1) : -1;
		}        

        return combinations[amount];
    }
};