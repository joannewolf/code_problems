#include <string>
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.length() == 0)
        	return 0;
        if (haystack.length() < needle.length())
        	return -1;

        int flag = 0;
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
        	if (haystack.substr(i, needle.length()) == needle)
        		return i;
        }
        return -1;
    }
};