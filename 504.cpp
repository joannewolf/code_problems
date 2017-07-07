class Solution {
public:
    string convertToBase7(int num) {
        if (num == 0)
            return "0";
        string result;
        bool positive = (num >= 0);
        num = abs(num);
        while (num != 0) {
            result.insert(result.begin(), (num % 7) + 48);
            num /= 7;
        }
        if (!positive)
            result.insert(result.begin(), '-');
        return result;
    }
};