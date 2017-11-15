class Solution {
public:
    int flipLights(int n, int m) {
        // button would not have effect is it's performed even times
        // button2 + button3 = button1's effect
        // thus, we can summary into 12 different scenarios, {odd, even}^4
        // in addition, we consider the situation when there's only few bulbs
        if (m == 0)
        	return 1;
        if (n == 1)
        	return 2;
        if (n == 2) {
        	if (m == 1)
        		return 3;
        	else
        		return 4;
        }
        if (m == 1)
        	return 4;
        if (m == 2)
        	return 7;
        return 8;
    }
};