class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict = {}
        ransomNote_dict = {}
        for char in magazine:
            if char in magazine_dict:
                magazine_dict[char] += 1
            else:
                magazine_dict[char] = 1

        for char in ransomNote:
            if char in ransomNote_dict:
                ransomNote_dict[char] += 1
            else:
                ransomNote_dict[char] = 1

        for char in ransomNote_dict.keys():
            if char not in magazine_dict:
                return False
            elif ransomNote_dict[char] > magazine_dict[char]:
                return False

        return True
