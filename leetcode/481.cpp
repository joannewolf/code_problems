class Solution {
public:
	int magicalString(int n) {
		if (n <= 0)
			return 0;

		vector<int> nums({1, 2, 2});
		int flag = 2;

		while (nums.size() < n) {
			if (nums.back() == 1) {
				for (int i = 0; i < nums[flag]; i++)
					nums.emplace_back(2);
			}
			else {
				for (int i = 0; i < nums[flag]; i++)
					nums.emplace_back(1);
			}
			flag ++;
		}

		int oneCount = 0;
		for (int i = 0; i < n; i++) {
			if (nums[i] == 1)
				oneCount ++;
		}

		return oneCount;
	}
};