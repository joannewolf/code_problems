class Solution {
public:
    int superPow(int a, vector<int>& b) {
    	if (b.size() == 0 || a == 1)
    		return 1;
    	if (a == 0)
    		return 0;

    	int dividend = 1337;
    	int base = a % dividend, result = 1;
    	for (int i = b.size() - 1; i >= 0; i--) {
    		for (int j = 0; j < b[i]; j++) {
    			result *= base;
    			result %= dividend;
    		}
    		int nextBase = 1;
    		for (int j = 0; j < 10; j++) {
    			nextBase *= base;
    			nextBase %= dividend;
    		}
    		base = nextBase;
    	}

    	return result;
    }
};