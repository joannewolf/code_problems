class Solution {
public:
    int calculate(string s) {
    	if (s.empty())
    		return 1;

        vector<int> numbers;
        string operators;
        string num;
        
        // parse all numbers and operators
        for (char c : s) {
        	if (c == ' ')
        		continue;
        	else if (isdigit(c))
        		num.push_back(c);
        	else {
        		numbers.push_back(stoi(num));
        		num.clear();
        		operators.push_back(c);
        	}
        }
        numbers.push_back(stoi(num));
        
        // do multiplication and division first
        for (int i = 0; i < operators.length(); i++) {
        	if (operators[i] == '*') {
        		numbers[i] = numbers[i] * numbers[i + 1];
        		numbers.erase(numbers.begin() + (i + 1));
        		operators.erase(operators.begin() + i);
        		i--;
        	}
        	else if (operators[i] == '/') {
        		numbers[i] = numbers[i] / numbers[i + 1];
        		numbers.erase(numbers.begin() + (i + 1));
        		operators.erase(operators.begin() + i);
        		i--;
        	}
        }
		
        // do addition and substraction
        for (int i = 0; i < operators.length(); i++) {
        	if (operators[i] == '+')
        		numbers[i + 1] = numbers[i] + numbers[i + 1];
        	else if (operators[i] == '-')
        		numbers[i + 1] = numbers[i] - numbers[i + 1];
        }
        return numbers.back();
    }
};