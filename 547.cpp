class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size(), circleCount = 0, checkCount = 0;
        vector<bool> checked(n, false);
		
        while (checkCount < n) {
        	for (int i = 0; i < n; i++) {
        		if (!checked[i]) {
        			circleCount ++;
        			stack<int> toBeChecked;
        			toBeChecked.emplace(i);
        			while (!toBeChecked.empty()) {
        				int temp = toBeChecked.top();
        				toBeChecked.pop();
        				checked[temp] = true;
        				checkCount ++;
        				for (int j = 0; j < n; j ++) {
        					if (M[temp][j] == 1 && !checked[j])
        						toBeChecked.emplace(j);
        				}
        			}
        		}
        	}
        }

        return circleCount;
    }
};