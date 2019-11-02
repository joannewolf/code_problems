#include <stack>
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
    	if (heights.size() == 0)
    		return 0;
        // for every element, take it as height of rectangle, and look for the furthest left/right index it can reach
        int n = heights.size(), maxRectArea = 0;
        stack<int> st;
        vector<int> rightBounds(n, -1), leftBounds(n, -1);

        // find every element's right bound
        for (int i = 0; i < n; i++) {
        	if (st.empty() || heights[st.top()] <= heights[i])
        		st.push(i);
        	else {
				while (!st.empty() && heights[st.top()] > heights[i]) {
					rightBounds[st.top()] = i - 1;
					st.pop();
				}
				st.push(i);
        	}
        }
        while (!st.empty()) {
        	rightBounds[st.top()] = n - 1;
        	st.pop();
        }

        // find every element's left bound
        for (int i = n - 1; i >= 0; i--) {
        	if (st.empty() || heights[st.top()] <= heights[i])
        		st.push(i);
        	else {
				while (!st.empty() && heights[st.top()] > heights[i]) {
					leftBounds[st.top()] = i + 1;
					st.pop();
				}
				st.push(i);
        	}
        }
        while (!st.empty()) {
        	leftBounds[st.top()] = 0;
        	st.pop();
        }
        
        // calculate every rectagle and find the Max one
        for (int i = 0; i < n; i++) 
        	maxRectArea = max(maxRectArea, heights[i] * (rightBounds[i] - leftBounds[i] + 1));
        return maxRectArea;
    }
};