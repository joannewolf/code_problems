class Solution {
public:
    int numTrees(int n) {
        vector<int> combinations;
        // combinations[i]: the # combinations when there's i nodes
        combinations.push_back(1);
        combinations.push_back(1);
        for (int i = 2; i <= n; i++) {
        	combinations.push_back(0);
        	for (int j = 0; j <= i - 1; j++)
        		combinations.back() += (combinations[j] * combinations[i - 1 - j]);
        }
        return combinations[n];
    }
};