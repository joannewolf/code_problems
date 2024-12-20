class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        ascii_a = ord('a')
        result = ""
        char_count = [0] * 26
        for char in s:
            char_count[ord(char) - ascii_a] += 1

        current = 25 # start from 'z'
        next = 24
        while current >= 0:
            if char_count[current] == 0:
                current -= 1
            elif char_count[current] <= repeatLimit:
                result += chr(ascii_a + current) * char_count[current]
                char_count[current] = 0
                current -= 1
            else:
                result += chr(ascii_a + current) * repeatLimit
                char_count[current] -= repeatLimit
                next = current - 1
                while next >= 0:
                    if char_count[next] == 0:
                        next -= 1
                    else:
                        result += chr(ascii_a + next)
                        char_count[next] -= 1
                        break
                if next == -1:
                    return result

        return result
