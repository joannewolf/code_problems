#include <string>
#include <math.h>
class Solution {
public:
    int nextGreaterElement(int n) {
        string num = to_string(n), tempNum;
        tempNum.push_back(num.back());
        for (int i = num.length() - 2; i >= 0; i--) {
        	if (num[i] < num[i + 1]) {
        		for (int j = 0; j < tempNum.length(); j++) {
        			if (tempNum[j] > num[i]) {
        				char c = tempNum[j];
        				tempNum[j] = num[i];
        				num[i] = c;
        				num.replace(num.begin() + i + 1, num.end(), tempNum);
        				long long tempAns = stoll(num);
        				return (tempAns <= INT_MAX) ? int(tempAns) : -1;
        			}
        		}
        	}
        	tempNum.push_back(num[i]);
        }
        return -1;
    }
};