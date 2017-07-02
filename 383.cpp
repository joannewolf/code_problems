class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if (ransomNote.length() == 0)
        	return true;
        if (ransomNote.length() > magazine.length())
        	return false;
       	
       	int flag1 = 0, flag2 = 0;
       	sort(ransomNote.begin(), ransomNote.end());
       	sort(magazine.begin(), magazine.end());
       	while (flag1 < ransomNote.length() && flag2 < magazine.length()) {
       		if (ransomNote[flag1] == magazine[flag2]) {
       			flag1 ++;
       			flag2 ++;
       		}
       		else if (ransomNote[flag1] > magazine[flag2])
       			flag2 ++;
       		else
       			return false;
       	}
       	return (flag1 == ransomNote.length());
    }
};