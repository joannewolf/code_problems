# get O(1), put O(1), use hash map and double linked-list
class ListNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key_to_node = {}
        self.capacity = capacity

        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.right = self.tail
        self.tail.left = self.head

    def _delete_node(self, node):
        node.left.right = node.right
        node.right.left = node.left

    # keep most recently used node at head
    def _move_to_head(self, node):
        node.right = self.head.right
        node.right.left = node
        self.head.right = node
        node.left = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key_to_node:
            return -1
        else:
            node = self.key_to_node[key]
            self._delete_node(node)
            self._move_to_head(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._delete_node(node)
            self._move_to_head(node)
            node.value = value
        elif len(self.key_to_node) < self.capacity:
            node = ListNode(key, value)
            self.key_to_node[key] = node
            self._move_to_head(node)
        else:
            # remove least recently used node
            self.key_to_node.pop(self.tail.left.key)
            self._delete_node(self.tail.left)
            # add new node to head
            node = ListNode(key, value)
            self.key_to_node[key] = node
            self._move_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)