#include <stack>
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;
        for (string s : tokens) {
        	if (s != "+" && s != "-" && s != "*" && s != "/")
        		nums.push(stoi(s));
        	else {
        		int latterNum = nums.top();
        		nums.pop();
        		int formerNum = nums.top();
        		nums.pop();
        		switch (s[0]) {
        			case '+':
        				nums.push(formerNum + latterNum);
        				break;
        			case '-':
        				nums.push(formerNum - latterNum);
        				break;
        			case '*':
        				nums.push(formerNum * latterNum);
        				break;
        			case '/':
        				nums.push(formerNum / latterNum);
        				break;
        		}
        	}
        }
        return nums.top();
    }
};