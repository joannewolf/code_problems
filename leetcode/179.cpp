#include <algorithm>
class Solution {
private:
	static bool mysort(string a, string b) {
		return (a + b > b + a);
	}
public:
    string largestNumber(vector<int>& nums) {
        if (nums.size() == 0)
        	return "";

        string result;
        vector<string> numsStrs;
        for (int i : nums) {
        	numsStrs.push_back(to_string(i));
        }
        
        sort(numsStrs.begin(), numsStrs.end(), mysort);
		if (numsStrs[0] == "0")
        	return "0";
		for (string s : numsStrs)
			result += s;
        return result;
    }
};