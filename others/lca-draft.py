

from collections import defaultdict
from math import log

class LCA:
    def __init__(self, root: int, edges: list):
        """
        - root(int): val of root
        - edges(list of edge): 
            - edge [int, int]: two endpoints on this edge
        """
        self.root = root
        self.node_to_nodes = self.get_node_to_nodes(edges)
        self.n = len(self.node_to_nodes)
        self.cin = dict() # the timestamp when enter a node, used for checking the parent
        self.cout = dict() # the timestamp when leave a node, used for checking the parent
        self.time = 0
        self.max_len = int(log(self.n+1, 2)) + 1 # maximum depth of the binary lifting
        self.bl = {} # binary_lifting
        self.build(self.root, self.root, set()) # build binary lifting

        
    def get_node_to_nodes(self, edges):
        node_to_nodes = defaultdict(list)
        for x, y in edges:
            node_to_nodes[x].append(y)
            node_to_nodes[y].append(x)
        return node_to_nodes
    
    def build(self, cur, parent, seen):
        """
        Build the binary lifting, and the relating components
            - binary lifting
            - cin
            - cout
        """
        if cur in seen:
            return
        seen.add(cur)
        self.cin[cur] = self.time
        self.time += 1
        
        # Build binary lifting of the current node
        self.bl[cur] = [cur] # 0-th: self
        self.bl[cur].append(parent) # 1-th
        for i in range(2, self.max_len+1):
            self.bl[cur].append(self.bl[self.bl[cur][i-1]][i-1])
            
        # Go to children nodes
        for nxt in self.node_to_nodes[cur]:
            self.build(nxt, cur, seen)

        self.cout[cur] = self.time
        self.time += 1

    def is_parent(self, p, q):
        """
        Check if the node-p is the parent of the node-q.
        """
        if self.cin[p] <= self.cout[q] and self.cout[p] >= self.cout[q]:
            return True
        return False
    
    def query(self, n1, n2):
        """Find LCA of n1 and n2
        Note: After the for loop, the n1 stop on the 1-th child of LCA
        """
        if self.is_parent(n1, n2):
            return n1
        if self.is_parent(n2, n1):
            return n2
        for d in range(self.max_len, 0, -1):
            p = self.bl[n1][d]
            if not self.is_parent(p, n2):
                n1 = p
        return self.bl[n1][1]