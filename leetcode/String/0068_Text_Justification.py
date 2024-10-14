class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        N = len(words)
        word_lens = []
        for w in words:
            word_lens.append(len(w))

        result = []
        line_width = word_lens[0]
        left, right = 0, 1
        while right < N:
            if line_width + (word_lens[right] + 1) <= maxWidth:
                line_width += (word_lens[right] + 1)
                right += 1
            else:
                # words[left : right] become one line
                intervals = right - left - 1
                spaces = maxWidth - sum(word_lens[left:right])
                line = words[left]
                if intervals == 0:
                    line += ' ' * spaces
                else:
                    for i in range(left + 1, right):
                        line += ' ' * (spaces // intervals + int(i - (left + 1) < spaces % intervals))
                        line += words[i]
                result.append(line)

                left = right
                line_width = word_lens[left]
                right += 1

        # justify last line
        tail_spaces = maxWidth - sum(word_lens[left:]) - (N - left - 1)
        line = words[left]
        for i in range(left + 1, N):
            line += ' ' + words[i]
        line += ' ' * tail_spaces
        result.append(line)

        return result
