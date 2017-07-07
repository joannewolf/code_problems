class Solution {
public:
    int distributeCandies(vector<int>& candies) {
        if (candies.size() == 0)
            return 0;
        int count = 1;
        sort(candies.begin(), candies.end());
        for (int i = 1; i < candies.size(); i++) {
            if (candies[i] != candies[i - 1])
                count ++;
        }
        return (count >= candies.size() / 2) ? (candies.size() / 2) : count;
    }
};