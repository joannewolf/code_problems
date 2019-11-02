class Solution {
private:
	vector<int> compute(vector<int> nums, vector<int> operators) {
		if (nums.size() == 0)
			return vector<int>();
		if (nums.size() == 1)
			return vector<int>(1, nums[0]);

		vector<int> result;
		for (int i = 0; i < operators.size(); i++) {
			vector<int> formerResult = compute(vector<int>(nums.begin(), nums.begin() + i + 1), vector<int>(operators.begin(), operators.begin() + i));
			vector<int> latterResult = compute(vector<int>(nums.begin() + i + 1, nums.end()), vector<int>(operators.begin() + i + 1, operators.end()));
			switch(operators[i]) {
				case 0:
					for (int i1 : formerResult) {
						for (int i2 : latterResult)
							result.push_back(i1 + i2);
					}
					break;
				case 1:
					for (int i1 : formerResult) {
						for (int i2 : latterResult)
							result.push_back(i1 - i2);
					}
					break;
				case 2:
					for (int i1 : formerResult) {
						for (int i2 : latterResult)
							result.push_back(i1 * i2);
					}
					break;
			}
		}
		return result;
	}
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> nums, operators;
        string temp;
        // operators: 0 -> '+', 1 -> '-', 2 -> '*'
        // deal with input string
        for (char c : input) {
        	switch(c) {
        		case '+':
        			operators.push_back(0);
        			nums.push_back(stoi(temp));
        			temp.clear();
        			break;
        		case '-':
        			operators.push_back(1);
        			nums.push_back(stoi(temp));
        			temp.clear();
        			break;
        		case '*':
        			operators.push_back(2);
        			nums.push_back(stoi(temp));
        			temp.clear();
        			break;
        		default:
        			temp.push_back(c);
        	}
        }
        nums.push_back(stoi(temp));

        return compute(nums, operators);
    }
};