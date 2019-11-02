#include <iostream>
#include <algorithm>
class Solution {
public:
    string multiply(string num1, string num2) {
        if (num1 == "0" || num2 == "0")
            return "0";
        string result = "";
        int n1 = num1.length(), n2 = num2.length();
        vector<string> tempProduct(10, ""); // num1 * 0 ~ 9
        tempProduct[0] = "0";
        for (int i = 1; i <= 9; i++) {
            int product = 0, carry = 0;
            for (int j = n1 - 1; j >= 0; j--) {
                product = (num1[j] - 48) * i + carry;
                tempProduct[i].insert(tempProduct[i].begin(), (product % 10) + 48);
                carry = product / 10;
            }
            while (carry != 0) {
                tempProduct[i].insert(tempProduct[i].begin(), (carry % 10) + 48);
                carry /= 10;
            }
        }

        for (int i = 0; i < num2.length(); i++) {
            string added = tempProduct[num2[n2 - 1 - i] - 48];
            string temp(i, '0');
            added += temp;
            int carry = 0, flagR = result.length() - 1, flagA = added.length() - 1;
            while (flagR >= 0 && flagA >= 0) {
                int sum = (result[flagR] - 48) + (added[flagA] - 48) + carry;
                result[flagR] = (sum % 10) + 48;
                carry = sum / 10;
                flagR --;
                flagA --;
            }
            while (flagR >= 0 && carry != 0) {
                int sum = (result[flagR] - 48) + carry;
                result[flagR] = (sum % 10) + 48;
                carry = sum / 10;
                flagR --;
            }
            while (flagA >= 0) {
                int sum = (added[flagA] - 48) + carry;
                result.insert(result.begin(), (sum % 10) + 48);
                carry = sum / 10;
                flagA --;
            }
            while (carry != 0) {
                result.insert(result.begin(), (carry % 10) + 48);
                carry /= 10;
            }
        }
        return result;
    }
};