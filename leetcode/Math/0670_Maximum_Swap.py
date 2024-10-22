class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        N = len(num_str)
        max_num_str = sorted(num_str, reverse=True)
        for i in range(N):
            if num_str[i] != max_num_str[i]:
                # swap current digit with the largest possible digit
                j = num_str.rfind(max_num_str[i])
                num_str = list(num_str)
                num_str[i], num_str[j] = num_str[j], num_str[i]
                break

        return int(''.join(num_str))
