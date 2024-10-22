# Trie
class Solution(object):
    def _compare(self, str1, str2):
        if len(str1) != len(str2):
            return len(str1) - len(str2)
        else:
            # lexicographical decreasing
            if str1 < str2:
                return 1
            else:
                return -1

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # sort words by length
        words = sorted(words, cmp=self._compare)
        longest_word = ''
        root = {}
        # insert word into trie only if every previous char are in the trie
        for word in words:
            N = len(word)
            all_pass = True
            current_node = root

            for i in range(N - 1):
                if not word[i] in current_node.keys():
                    all_pass = False
                    break
                else:
                    current_node = current_node[word[i]]

            if all_pass:
                current_node[word[-1]] = {}
                if len(word) >= len(longest_word):
                    longest_word = word

        return longest_word

# buckets
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_word_len = 30
        dict = []
        for _ in range(max_word_len + 2):
            dict.append(set())

        # categorize words by length
        dict[0].add('')
        for word in words:
            dict[len(word)].add(word)

        for i in range(1, max_word_len + 2):
            temp_set = dict[i].copy()
            for word in dict[i]:
                # remove invalid word
                if not word[:-1] in dict[i - 1]:
                    temp_set.remove(word)

            if not temp_set:
                return sorted(dict[i - 1])[0]
            else:
                dict[i] = temp_set
