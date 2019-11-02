#include <ctype.h>
class Solution {
private:
	bool isValidIPv4Address(string IP) {
		vector<string> tokens(1, "");
		for (char c : IP) {
			if (c == '.') {
				tokens.push_back("");
			}
			else if (!isdigit(c)) {
				return false;
			}
			else {
				tokens.back().push_back(c);
			}
		}
		if (tokens.size() != 4) {
			return false;
		}
		for (string token : tokens) {
			if (token.length() == 0 || token.length() > 3 || (token[0] == '0' && token.length() != 1) || stoi(token) > 255 || stoi(token) < 0) {
				return false;
			}
		}
		return true;
	}
	bool isValidIPv6Address(string IP) {
		vector<string> tokens(1, "");
		for (char c : IP) {
			if (c == ':') {
				tokens.push_back("");
			}
			else if (!isalnum(c) || (islower(c) && c > 'f') || (isupper(c) && c > 'F')) {
				return false;
			}
			else {
				tokens.back().push_back(c);
			}
		}
		if (tokens.size() != 8) {
			return false;
		}
		for (string token : tokens) {
			if (token.length() == 0 || token.length() > 4) {
				return false;
			}
		}
		return true;
	}
public:
    string validIPAddress(string IP) {
        if (isValidIPv4Address(IP))
        	return "IPv4";
        else if (isValidIPv6Address(IP))
        	return "IPv6";
        else
        	return "Neither";
    }
};