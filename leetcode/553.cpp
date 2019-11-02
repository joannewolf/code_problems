// O(N), use math, solution must be a/(b/c/...)
class Solution {
public:
    string optimalDivision(vector<int>& nums) {
    	if (nums.size() == 1)
    		return to_string(nums[0]);
    	if (nums.size() == 2)
    		return (to_string(nums[0]) + "/" + to_string(nums[1]));
    	string result = to_string(nums[0]) + "/(";
    	for (int i = 1; i < nums.size() - 1; i++)
    		result += (to_string(nums[i]) + "/");
    	result += (to_string(nums.back()) + ")");
    	return result;
    }
};

// O(N!), brute-force
class Solution {
private:
    typedef struct {
        float maxNum, minNum;
        string maxStr, minStr;
    } T;
    T getOptimalDivision(vector<int> nums) {
        T t;
        if (nums.size() == 1) {
            t.maxNum = nums[0];
            t.minNum = nums[0];
            t.maxStr = to_string(nums[0]);
            t.minStr = to_string(nums[0]);
            return t;
        }
        t.maxNum = numeric_limits<float>::min();
        t.minNum = numeric_limits<float>::max();
        for (int i = 1; i < nums.size(); i++) {
            T left = getOptimalDivision(vector<int>(nums.begin(), nums.begin() + i));
            T right = getOptimalDivision(vector<int>(nums.begin() + i, nums.end()));
            if (t.minNum > left.minNum / right.maxNum) {
                t.minNum = left.minNum / right.maxNum;
                t.minStr = left.minStr + "/" + ((i != nums.size() - 1) ? "(" : "") + right.maxStr + ((i != nums.size() - 1) ? ")" : "");
            }
            if (t.maxNum < left.maxNum / right.minNum) {
                t.maxNum = left.maxNum / right.minNum;
                t.maxStr = left.maxStr + "/" + ((i != nums.size() - 1) ? "(" : "") + right.minStr + ((i != nums.size() - 1) ? ")" : "");
            }
        }
        return t;
    }
public:
    string optimalDivision(vector<int>& nums) {
        return getOptimalDivision(nums).maxStr;
    }
};