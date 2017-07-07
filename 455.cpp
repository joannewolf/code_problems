class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        if (g.size() == 0 || s.size() == 0)
            return 0;
        int count = 0, flagG = 0, flagS = 0;
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        while (flagG < g.size() && flagS < s.size()) {
            if (s[flagS] >= g[flagG]) {
                count ++;
                flagG ++;
                flagS ++;
            }
            else
                flagS ++;
        }
        return count;
    }
};