#include <stdlib.h>
class Solution {
private:
	string alphanum = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	int hashLength = 6;
	map<string, string> hashToURL, URLToHash;
public:

    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        if (URLToHash.find(longUrl) == URLToHash.end()) {
        	string newHash;
        	for (int i = 0; i < hashLength; i++)
		        newHash += alphanum[rand() % alphanum.length()];
		    URLToHash[longUrl] = newHash;
		    hashToURL[newHash] = longUrl;
		    return ("http://tinyurl.com/" + newHash);
        }
        else
		    return ("http://tinyurl.com/" + URLToHash[longUrl]);
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
    	string hash = shortUrl.substr(strlen("http://tinyurl.com/"));
    	return hashToURL[hash];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));