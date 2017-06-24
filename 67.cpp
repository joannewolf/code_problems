class Solution {
public:
    string addBinary(string a, string b) {
        int flagA = a.length() - 1, flagB = b.length() - 1, carry = 0;
        string result;
        while (flagA >= 0 && flagB >= 0) {
        	int temp = (a[flagA] - 48) + (b[flagB] - 48) + carry;
        	carry = temp / 2;
        	result.insert(result.begin(), (temp % 2) + 48);
        	flagA --;
        	flagB --;
        }
        while (flagA >= 0) {
        	int temp = (a[flagA] - 48) + carry;
        	carry = temp / 2;
        	result.insert(result.begin(), (temp % 2) + 48);
        	flagA --;
        }
        while (flagB >= 0) {
			int temp = (b[flagB] - 48) + carry;
        	carry = temp / 2;
        	result.insert(result.begin(), (temp % 2) + 48);
        	flagB --;
        }
        if (carry != 0)
        	result.insert(result.begin(), carry + 48);

        return result;
    }
};