#include <map>
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> result;
        if (s.length() < p.length())
            return result;
        
        map<char, int> letters, temp;
        // save p's letters
        sort(p.begin(), p.end());
        for (int i = 0; i < p.length(); i++) {
            if (letters.find(p[i]) == letters.end())
                letters[p[i]] = 1;
            else
                letters[p[i]] ++;
        }

        // find anagrams
        for (int i = 0; i < p.length(); i++) {
            if (temp.find(s[i]) == temp.end())
                temp[s[i]] = 1;
            else
                temp[s[i]] ++;
        }
        for (int i = 0; i <= s.length() - p.length(); i++) {
            // check if is anagram
            bool isAnagram = true;
            for (map<char, int>::iterator it = letters.begin(); it != letters.end(); it++) {
                if (temp.find(it -> first) == temp.end() || temp[it -> first] != it -> second) {
                    isAnagram = false;
                    break;
                }
            }
            if (isAnagram)
                result.push_back(i);
            // update temp, erase first char and add next char
            temp[s[i]] --;
            if (i != s.length() - p.length()) {
                if (temp.find(s[i + p.length()]) == temp.end())
                    temp[s[i + p.length()]] = 1;
                else
                    temp[s[i + p.length()]] ++;
            }
        }

        return result;
    }
};