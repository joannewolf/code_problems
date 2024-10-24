#include <ctype.h>
#include <climits>
class Solution {
public:
    int myAtoi(string str) {
    	if (str.length() == 0)
    		return 0;

        long long result = 0;
        int symbol = 1;
        while (str[0] == ' ')
        	str.erase(str.begin());        
        for (int i = 0; i < str.length(); i++) {
        	if (i == 0 && str[0] == '-')
        		symbol = -1;
        	else if (i == 0 && str[0] == '+')
        		symbol = 1;
        	else if (isdigit(str[i])) {
        		result *= 10;
        		result += (str[i] - 48);
        	}
        	else
        		break;
        	if (result * symbol > INT_MAX)
        		return INT_MAX;
        	if (result * symbol < INT_MIN)
        		return INT_MIN;
        }
        return (result * symbol);
    }
};