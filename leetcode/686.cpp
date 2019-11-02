class Solution {
public:
    int repeatedStringMatch(string A, string B) {
        int lengthA = A.length(), lengthB = B.length();

        int n = lengthB / lengthA;
        string temp;
        for (int i = 0; i < n; i++)
        	temp += A;

        if (lengthB % lengthA == 0) {
        	// n or n + 1
        	if (temp.find(B) != -1)
        		return n;

        	temp += A;
        	if (temp.find(B) != -1)
        		return (n + 1);
        }
        else if (lengthB % lengthA == 1) {
        	// n + 1
        	temp += A;
        	if (temp.find(B) != -1)
        		return (n + 1);
        }
        else {
        	// n + 1 or n + 2
        	temp += A;
        	if (temp.find(B) != -1)
        		return (n + 1);

        	temp += A;
        	if (temp.find(B) != -1)
        		return (n + 2);
        }

        return -1;
    }
};