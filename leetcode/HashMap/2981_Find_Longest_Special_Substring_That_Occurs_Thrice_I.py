class Solution(object):
    def maximumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        s += '.'
        current_char = s[0]
        current_count = 0
        substr_dict = {}
        for char in s:
            if char == current_char:
                current_count += 1
            else:
                if current_char not in substr_dict:
                    substr_dict[current_char] = [current_count]
                else:
                    substr_dict[current_char].append(current_count)
                current_char = char
                current_count = 1

        max_len = 0
        for substr_lens in substr_dict.values():
            substr_lens.sort()
            if substr_lens[-1] >= 3:
                max_len = max(max_len, substr_lens[-1] - 2)
            if len(substr_lens) >= 2:
                if substr_lens[-2] < substr_lens[-1]:
                    max_len = max(max_len, substr_lens[-2])
                else:
                    max_len = max(max_len, substr_lens[-2] - 1)
            if len(substr_lens) >= 3:
                max_len = max(max_len, substr_lens[-3])

        return max_len if max_len > 0 else -1
