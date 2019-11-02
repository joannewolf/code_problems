// DFS
class Solution {
private:
	int dfs(int index, int count, vector<int> debt) {
		// find min number of transactions to settle starting from debt[s]
		
		// find the next non-zero debt
		while (index < debt.size() && debt[index] == 0)
			index ++;
		
		int result = INT_MAX;
		for (int i = index + 1; i < debt.size(); i++) {
			// try every different sign debt to counterbalance
			if (debt[i] * debt[index] < 0) {
				debt[i] += debt[index];
				result = min(result, dfs(index + 1, count + 1, debt));
				debt[i] -= debt[index];
			}
		}

		return (result != INT_MAX) ? result : count;
	}
public:
	int minTransfers(vector<vector<int>>& transactions) {
		unordered_map<int, int> balance;

		// calculate everyone's balance
		for (vector<int> transaction : transactions) {
			balance[transaction[0]] -= transaction[2];
			balance[transaction[1]] += transaction[2];
		}

		vector<int> debt;
		for (auto it = balance.begin(); it != balance.end(); it ++) {
			debt.emplace_back(it -> second);
			cout << (it -> second) << " ";
		}
		cout << endl;
		return dfs(0, 0, debt);
	}
};

// DFS + optimization
class Solution {
private:
	int dfs(int index, int count, vector<int> debt) {
		// find min number of transactions to settle starting from debt[s]
		
		// find the next non-zero debt
		while (index < debt.size() && debt[index] == 0)
			index ++;
		
		int result = INT_MAX;
		for (int i = index + 1; i < debt.size(); i++) {
			// try every different sign debt to counterbalance
			if (debt[i] * debt[index] < 0) {
				debt[i] += debt[index];
				result = min(result, dfs(index + 1, count + 1, debt));
				debt[i] -= debt[index];
			}
		}

		return (result != INT_MAX) ? result : count;
	}
public:
	int minTransfers(vector<vector<int>>& transactions) {
		unordered_map<int, int> balance;

		// calculate everyone's balance
		for (vector<int> transaction : transactions) {
			balance[transaction[0]] -= transaction[2];
			balance[transaction[1]] += transaction[2];
		}

		int count = 0;
		vector<int> debt;
		// collect all non-zero balances
		for (auto it = balance.begin(); it != balance.end(); it ++) {
			if (it -> second != 0)
				debt.emplace_back(it -> second);
		}

		// find matched pairs
		for (int i = 0; i < debt.size(); i++) {
			for (int j = i + 1; j < debt.size(); j++) {
				if (debt[i] == -debt[j]) {
					count ++;
					debt.erase(debt.begin() + j);
					debt.erase(debt.begin() + i);
					i --;
					break;
				}
			}
		}

		return count + dfs(0, 0, debt);
	}
};

// brute-force try every permutation and find the minimum # transaction
class Solution {
private:
	void getNextPermutation(vector<int> &nums) {
        // rearrange to next greater order
        for (int i = nums.size() - 1; i > 0; i--) {
            if (nums[i] > nums[i - 1]) {
                sort(nums.begin() + i, nums.end());
                for (int j = i; i < nums.size(); j++) {
                    if (nums[j] > nums[i - 1]) {
                        int temp = nums[j];
                        nums[j] = nums[i - 1];
                        nums[i - 1] = temp;
                        break;
                    }
                }
                return;
            }
        }
        // rearrange to lowest order
        for (int i = 0; i < nums.size() / 2; i++) {
            int temp = nums[i];
            nums[i] = nums[nums.size() - 1 - i];
            nums[nums.size() - 1 - i] = temp;
        }
        return;
    }
public:
	int minTransfers(vector<vector<int>>& transactions) {
		unordered_map<int, int> balance;

		// calculate everyone's balance
		for (vector<int> transaction : transactions) {
			balance[transaction[0]] -= transaction[2];
			balance[transaction[1]] += transaction[2];
		}

		int result = INT_MAX;
		vector<int> positive, negative;
		// collect all non-zero balances
		for (auto it = balance.begin(); it != balance.end(); it ++) {
			if (it -> second > 0)
				positive.emplace_back(it -> second);
			else if (it -> second < 0)
				negative.emplace_back(it -> second);
		}

		int permutationCount = 1;
		vector<int> negativeIndex;
		for (int i = 1; i <= negative.size(); i++) {
			permutationCount *= i;
			negativeIndex.emplace_back(i - 1);
		}

		for (int i = 0; i < permutationCount; i++) {
			int count = 0, sum = 0, positiveFlag = 0, negativeFlag = 0;
			while (positiveFlag < positive.size() || negativeFlag < negative.size()) {
				if (sum + negative[negativeIndex[negativeFlag]] < 0) {
					sum += positive[positiveFlag];
					positiveFlag ++;
				}
				else {
					sum += negative[negativeIndex[negativeFlag]];
					negativeFlag ++;
				}
				if (sum != 0)
					count ++;
			}

			result = min(result, count);
			getNextPermutation(negativeIndex);
		}

		return result;
	}
};