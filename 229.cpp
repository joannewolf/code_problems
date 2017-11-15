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