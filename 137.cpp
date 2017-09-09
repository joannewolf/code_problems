class Solution {
public:
    int singleNumber(vector<int>& nums) {
        /* 
        3 states need 2 bits, 3 same nums will cause state [0, 0]
        current state	input	next state
        a b				c 		a b
        0 0				0/1		0 0/0 1
        0 1				0/1		0 1/1 0
        1 0				0/1		1 0/0 0
        a = ~a & b & c + a & ~b & ~c
        b = ~a & ~b & c + ~a & b & ~c
        at the end, return number which bit state is 01 | 10 -> 1, 00 -> 0
		*/
    	int a = 0, b = 0;
    	for (int c : nums) {
    		int tempA = (~a & b & c) | (a & ~b & ~c);
    		b = (~a & ~b & c) | (~a & b & ~c);
    		a = tempA;
    	}
    	return (a | b);
    }
};