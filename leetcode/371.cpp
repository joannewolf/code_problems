class Solution {
public:
    int getSum(int a, int b) {
        int sum = a ^ b, carry = a & b;
        while (carry != 0) {
        	carry <<= 1;
        	a = sum;
        	b = carry;
        	sum = a ^ b;
        	carry = a & b;
        }
        return sum;
    }
};