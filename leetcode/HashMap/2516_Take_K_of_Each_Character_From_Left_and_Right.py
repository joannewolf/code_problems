class Solution(object):
    def takeCharacters(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        N = len(s)
        count_a, count_b, count_c = 0, 0, 0
        for char in s:
            if char == 'a':
                count_a += 1
            elif char == 'b':
                count_b += 1
            elif char == 'c':
                count_c += 1

        if count_a < k or count_b < k or count_c < k:
            return -1
        if k == 0:
            return 0

        # for each prefix s[:left+1], find the min suffix s[right:]
        prefix_char_dict = {'a': 0, 'b': 0, 'c': 0}
        suffix_char_dict = {'a': 0, 'b': 0, 'c': 0}
        right = N - 1
        for i in range(N - 1, -1, -1):
            suffix_char_dict[s[i]] += 1
            if suffix_char_dict['a'] >= k and suffix_char_dict['b'] >= k and suffix_char_dict['c'] >= k:
                right = i
                break

        min_len = N - right # without prefix
        for left in range(N):
            prefix_char_dict[s[left]] += 1
            while right < N:
                if suffix_char_dict[s[right]] + prefix_char_dict[s[right]] > k:
                    suffix_char_dict[s[right]] -= 1
                    right += 1
                else:
                    break
            min_len = min(min_len, (left + 1) + (N - right))

        return min_len
