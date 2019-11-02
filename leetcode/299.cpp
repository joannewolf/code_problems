#include <math.h>
class Solution {
public:
    string getHint(string secret, string guess) {
    	int a = 0, b = 0, n = secret.length();
    	map<int, int> secretNum, guessNum;

    	for (int i = 0; i < n; i++) {
    		if (secret[i] == guess[i])
    			a ++;
    		else {
    			if (secretNum.find(secret[i]) == secretNum.end())
	    			secretNum[secret[i]] = 1;
	    		else
	    			secretNum[secret[i]] ++;

	    		if (guessNum.find(guess[i]) == guessNum.end())
	    			guessNum[guess[i]] = 1;
	    		else
	    			guessNum[guess[i]] ++;
    		} 
    	}

    	for (auto it = guessNum.begin(); it != guessNum.end(); it++) {
    		if (secretNum.find(it -> first) != secretNum.end())
    			b += min(secretNum[it -> first], it -> second);
    	}

    	return (to_string(a) + "A" + to_string(b) + "B");
    }
};