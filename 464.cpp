#include <algorithm>
class Solution {
private:
    vector<int> states; // -1: lose, 0: unchecked, 1: win
    int currentState, n;
    int check(int desiredTotal) {
    	if (desiredTotal <= 0)
    		return -1;
    	if (states[currentState] == 0){
    		for (int i = 1; i <= n; i++) {
	    		int temp = 1;
	    		temp <<= (i - 1);
	    		// if not num i is not used
    	    	if ((currentState & temp) == 0) {
	    			currentState += temp;
	    			// check whether it lead to win, i.e. the other player lose
	    			int tempResult = check(desiredTotal - i);
	   				currentState -= temp;
	   				if (tempResult == -1) {
	   					states[currentState] = 1;
	   					return 1;
	   				}
    	    	}
    	   	}
    	   	states[currentState] = -1;
    	}
    	return states[currentState];
    }

public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        int sum = (1 + maxChoosableInteger) * maxChoosableInteger / 2;        
        if (sum < desiredTotal)
        	return false;
        if (desiredTotal <= 0)
        	return true;

        // record states of used/unused numbers and their result
        states = vector<int>(pow(2, maxChoosableInteger), 0);
        currentState = 0;
        n = maxChoosableInteger;
        return (check(desiredTotal) > 0);
    }
};