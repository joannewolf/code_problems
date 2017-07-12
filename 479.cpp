#include <algorithm>
#include <math.h>
#include <string>
#include <iostream>
class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1)
            return 9;
        // product of two n-digit numbers is 2n-digits, try all possible palindromes and check if it's product of 2 n-digits numbers
        int upperBound = pow(10, n) - 1, lowerBound = upperBound / 10;
        for (int i = upperBound; i > lowerBound; i--) {
            string s = to_string(i);
            reverse(s.begin(), s.end());
            s = to_string(i) + s;
            long long ll = stoll(s);
            for (long long j = upperBound; j * j >= ll; j--) {
                if (ll % j == 0 && (ll / j) <= upperBound)
                    return (int)(ll % 1337);
            }
        }
    }
};