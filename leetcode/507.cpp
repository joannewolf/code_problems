class Solution {
public:
    bool checkPerfectNumber(int num) {
        if (num <= 1)
            return false;
        vector<int> factors;
        int sum = 0;
        // collect all factors of number
        factors.push_back(1);
        for (int i = 2; i * i <= num; i++) {
            if (num % i == 0) {
                factors.push_back(i);
                if (num / i != i)
                    factors.push_back(num / i);
            }
        }
        // check if sum of factors = number
        for (int i = 0; i < factors.size(); i++) {
            printf("%d ", factors[i]);
            sum += factors[i];
        }
        return (sum == num);
    }
};