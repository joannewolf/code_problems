class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> uglyNumbers;
        int flag2 = 0, flag3 = 0, flag5 = 0;
        uglyNumbers.push_back(1);
        for (int i = 1; i < n; i++) {
        	int temp2 = uglyNumbers[flag2] * 2, temp3 = uglyNumbers[flag3] * 3, temp5 = uglyNumbers[flag5] * 5;
        	int next = min(min(temp2, temp3), temp5);
        	uglyNumbers.push_back(next);
        	if (temp2 == next)
        		flag2 ++;
        	if (temp3 == next)
        		flag3 ++;
        	if (temp5 == next)
        		flag5 ++;
        }
        return uglyNumbers.back();
    }
};