class Solution {
public:
    string getPermutation(int n, int k) {
    	vector<char> unusedNums;
        string result;
        int flag = 1, countdown = n;

        for (int i = 1; i <= n; i++) {
        	unusedNums.push_back(i + 48);
        	flag *= i;
        }

        k -= 1;
        flag /= countdown;
        for (int i = 0; i < n - 1; i++) {
        	result.push_back(unusedNums[k / flag]);
        	unusedNums.erase(unusedNums.begin() + (k / flag));
        	k %= flag;
        	countdown --;
       		flag /= countdown;
        }
        result.push_back(unusedNums[0]);
        return result;
    }
};