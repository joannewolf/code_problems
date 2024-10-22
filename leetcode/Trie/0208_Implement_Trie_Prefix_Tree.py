class Trie(object):

    class TrieNode(object):
        def __init__(self, val=''):
            self.val = val
            self.is_end_of_word = False
            self.children = {}

    def __init__(self):
        self.root = self.TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for char in word:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                new_node = self.TrieNode(char)
                current_node.children[char] = new_node
                current_node = new_node

        current_node.is_end_of_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for char in word:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                return False

        return current_node.is_end_of_word

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for char in prefix:
            if char in current_node.children.keys():
                current_node = current_node.children[char]
            else:
                return False

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)