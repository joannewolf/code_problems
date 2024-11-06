class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        N, M = len(word1), len(word2)
        if N != M:
            return False

        char_dict1 = {}
        char_dict2 = {}
        for char in word1:
            if char in char_dict1:
                char_dict1[char] += 1
            else:
                char_dict1[char] = 1
        for char in word2:
            if char in char_dict2:
                char_dict2[char] += 1
            else:
                char_dict2[char] = 1

        char_set1 = set(char_dict1.keys())
        char_set2 = set(char_dict2.keys())
        char_count1 = sorted(char_dict1.values())
        char_count2 = sorted(char_dict2.values())

        if char_set1 != char_set2:
            return False
        else:
            return (char_count1 == char_count2)
