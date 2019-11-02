#include <algorithm>
class Solution {
public:
    string addStrings(string num1, string num2) {
        string ans;
        int flag1 = num1.length() - 1, flag2 = num2.length() - 1, carry = 0;
        while (flag1 >= 0 || flag2 >= 0) {
            int temp = carry;
            if (flag1 >= 0) {
                temp += (num1[flag1] - 48);
                flag1 --;
            }
            if (flag2 >= 0) {
                temp += (num2[flag2] - 48);
                flag2 --;
            }
            ans.insert(ans.begin(), (temp % 10) + 48);
            carry = temp / 10;
        }
        if (carry != 0)
            ans.insert(ans.begin(), carry + 48);

        return ans;
    }
};