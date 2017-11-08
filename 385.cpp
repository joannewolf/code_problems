#include <ctype.h>
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
public:
    NestedInteger deserialize(string s) {
        stack<NestedInteger> st;
        string tempStr;

        for (char c : s) {
        	if (isdigit(c) || c == '-') {
        		tempStr += c;
        	}
        	else if (c == '[') {
        		st.emplace(NestedInteger());
        	}
        	else if (c == ']') {
        		if (!tempStr.empty()) {
        			st.top().add(NestedInteger(stoi(tempStr)));
	        		tempStr.clear();
        		}

        		NestedInteger lastNI = st.top();
        		st.pop();
        		if (st.empty()) {
        			return lastNI;
        		}
        		else {
        			st.top().add(lastNI);
        		}
        	}
        	else if (c == ',') {
        		if (!tempStr.empty()) {
        			st.top().add(NestedInteger(stoi(tempStr)));
        			tempStr.clear();
        		}
        	}
        }

        if (!tempStr.empty())
       		return NestedInteger(stoi(tempStr));
    }
};