# O(N^3), TLE
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        strs1 = []
        strs2 = []
        for i in arr1:
            strs1.append(str(i))
        for i in arr2:
            strs2.append(str(i))

        max_lcp = 0
        for i in range(len(strs1)):
            for j in range(len(strs2)):
                min_len = min(len(strs1[i]), len(strs2[j]))
                lcp = min_len
                for x in range(min_len):
                    if strs1[i][x] != strs2[j][x]:
                        lcp = x
                        break

                max_lcp = max(max_lcp, lcp)

        return max_lcp

# O(N^2), trie
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # build trie using arr1
        trie1 = {}
        for i in arr1:
            s = str(i)
            current_node = trie1
            for char in s:
                if char not in current_node:
                    current_node[char] = {}
                current_node = current_node[char]

        # for each str in arr2, find the lcp in trie1
        max_lcp = 0
        for i in arr2:
            lcp = 0
            s = str(i)
            current_node = trie1
            for char in s:
                if char in current_node:
                    lcp += 1
                    current_node = current_node[char]
                else:
                    break
            max_lcp = max(max_lcp, lcp)

        return max_lcp


# O(N^2), set
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # put all possible prefix of arr1 in set
        prefix1 = set()
        for i in arr1:
            s = str(i)
            for x in range(len(s) + 1):
                prefix1.add(s[:x])

        # for each str in arr2, find the max prefix in set
        max_lcp = 0
        for i in arr2:
            s = str(i)
            lcp = len(s)
            for x in range(1, len(s) + 1):
                if s[:x] not in prefix1:
                    lcp = x - 1
                    break
            max_lcp = max(max_lcp, lcp)

        return max_lcp
