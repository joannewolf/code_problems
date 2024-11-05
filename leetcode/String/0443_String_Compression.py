class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars += ' ' # for triggering final compression
        current = chars[0]
        count = 1
        N = len(chars)

        i = 1
        while i < N:
            if chars[i] == current:
                count += 1
                del chars[i]
                N -= 1
            else:
                if count == 1:
                    current = chars[i]
                    i += 1
                else:
                    digit = 0
                    while count != 0:
                        chars.insert(i, str(count % 10))
                        count //= 10
                        digit += 1
                    N += digit
                    i += digit
                    current = chars[i]
                    count = 1
                    i += 1

        return i - 1
