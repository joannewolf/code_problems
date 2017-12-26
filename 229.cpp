// O(1) space, Boyer-Moore Majority Vote algorithm
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
		int candidate1 = -1, candidate2 = -1, count1 = 0, count2 = 0;
		for (int i : nums) {
			if (candidate1 == i)
				count1 ++;
			else if (candidate2 == i)
				count2 ++;
			else if (count1 == 0) {
				candidate1 = i;
				count1 = 1;
			}
			else if (count2 == 0) {
				candidate2 = i;
				count2 = 1;
			}
			else {
				count1 --;
				count2 --;
			}
		}

		vector<int> result;
		int n = nums.size();
		count1 = 0;
		count2 = 0;
		for (int i : nums) {
			if (i == candidate1)
				count1 ++;
			else if (i == candidate2)
				count2 ++;
		}
		if (count1 > n / 3)
			result.emplace_back(candidate1);
		if (count2 > n / 3)
			result.emplace_back(candidate2);

		return result;
    }
};

// O(N) space, brute-force
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
		map<int, int> counts;
		for (int i : nums) {
			if (counts.find(i) == counts.end())
				counts[i] = 1;
			else
				counts[i]++;
		}

		vector<int> result;
		int n = nums.size();
		for (auto it = counts.begin(); it != counts.end(); it++) {
			if (it -> second > n / 3)
				result.emplace_back(it -> first);
		}
		return result;
    }
};