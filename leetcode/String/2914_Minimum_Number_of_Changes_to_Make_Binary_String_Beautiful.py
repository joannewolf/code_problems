class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '.' # for triggering final count
        N = len(s)
        char_count = []
        current = s[0]
        count = 1
        for i in range(1, N):
            if s[i] == current:
                count += 1
            else:
                char_count.append(count)
                current = s[i]
                count = 1

        M = len(char_count)
        odd_count_index = []
        # only need to change odd..even..odd this kind of digits
        # odd_count_index should have even number of elements, cuz s has even length
        for i in range(M):
            if char_count[i] % 2 == 1:
                odd_count_index.append(i)

        K = len(odd_count_index)
        result = 0
        for i in range(0, K, 2):
            result += (odd_count_index[i+1] - odd_count_index[i])
        return result
