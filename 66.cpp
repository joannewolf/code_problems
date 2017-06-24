class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        // plus one
        digits.back() += 1;

        int carry = 0;
        for (int i = digits.size() - 1; i >= 0; i--) {
        	digits[i] += carry;
        	carry = digits[i] / 10;
        	digits[i] %= 10;
        }
        if (carry != 0)
        	digits.insert(digits.begin(), carry);
        return digits;
    }
};