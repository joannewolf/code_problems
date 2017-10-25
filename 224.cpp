#include <stack>
#include <string>
class Solution {
public:
    int calculate(string s) {
        stack<int> numbers;
        stack<char> operators;
        string num;
        numbers.push(0);
        operators.push('+');
        for (char c : s) {
        	if (c == ' ')
        		continue;
        	else if (isdigit(c))
        		num.push_back(c);
        	else if (c == '+' || c == '-') {
        		if (!num.empty()) {
        			if (operators.top() == '+')
	        			numbers.top() += stoi(num);
	        		else
	        			numbers.top() -= stoi(num);
	       			operators.top() = c;
	        		num.clear();
        		}
        		else
        			operators.push(c);
        	}
        	else if (c == '(') {
        		numbers.push(0);
        		operators.push('+');
        	}
        	else if (c == ')') {
	        	if (!num.empty()){
	        		if (operators.top() == '+')
	        			numbers.top() += stoi(num);
	        		else
	        			numbers.top() -= stoi(num);
	        		num.clear();
	        		operators.pop();
	        	}
	        	int temp = numbers.top();
        		numbers.pop();
        		if (operators.top() == '+')
        			numbers.top() += temp;
        		else
        			numbers.top() -= temp;
        		operators.pop();
        	}
        }
        if (!num.empty()) {
        	if (operators.top() == '+')
				numbers.top() += stoi(num);
			else
				numbers.top() -= stoi(num);
        }
        return numbers.top();
    }
};