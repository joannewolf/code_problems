class Solution {
public:
    string toHex(int num) {
        if (num == 0)
            return "0";
        string result;
        unsigned int n = num;
        while (n != 0) {
            if (n % 16 >= 0 && n % 16 < 10)
                result.insert(result.begin(), (n % 16) + 48);
            else {
                switch (n % 16) {
                    case 10:
                        result.insert(result.begin(), 'a');
                        break;
                    case 11:
                        result.insert(result.begin(), 'b');
                        break;
                    case 12:
                        result.insert(result.begin(), 'c');
                        break;
                    case 13:
                        result.insert(result.begin(), 'd');
                        break;
                    case 14:
                        result.insert(result.begin(), 'e');
                        break;
                    case 15:
                        result.insert(result.begin(), 'f');
                        break;
                }
            }
            n /= 16;
        }
        return result;
    }
};