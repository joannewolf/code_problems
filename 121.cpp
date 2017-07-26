class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1)
            return 0;
        int minLocal = prices[0], result = 0;
        for (int i = 0; i < prices.size(); i++) {
            if (prices[i] < minLocal)
                minLocal = prices[i];
            if (prices[i] - minLocal > result)
                result = prices[i] - minLocal;
        }
        return result;
    }
};