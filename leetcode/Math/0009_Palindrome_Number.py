class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        N = len(x_str)
        i, j = 0, N - 1
        for _ in range(N // 2):
            if x_str[i] != x_str[j]:
                return False
            i += 1
            j -= 1
        return True

# without converting to str
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        tens = [] # at most 10 digits
        for i in range(11):
            tens.append(pow(10, i))

        # get number of digit
        N = 0
        for i in range(11):
            if x // tens[i] == 0:
                N = i
                break
        # print('digit', N)

        # get left half of number and compare
        half_N = N // 2
        left_num = x // tens[N - half_N]
        right_num = x % tens[half_N]
        # print('left', left_num, 'right', right_num)
        left_num_reverse = 0
        for i in range(half_N):
            current_digit = left_num % 10
            left_num_reverse += current_digit * tens[half_N - i - 1]
            left_num //= 10

        # print('left reverse', left_num_reverse)
        return (left_num_reverse == right_num)
