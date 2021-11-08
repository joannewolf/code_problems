##### Floyd–Warshall algorithm
# For finding all pair of shortest paths in a directed weighted graph with positive or negative edge weights (but with no negative cycles)
# If there exists a negative-length path from i back to i, after the algorithm, dist[i][i] will be negative
# Using DP, O(V^3)
dist = [[INF] * V for i in range(V)]
next = [[None] * V for i in range(V)]

for (u, v) in edges:
    dist[u][v] = weight[u][v]
    next[u][v] = v
for v in vertices:
    dist[v][v] = 0
    next[v][v] = v
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                next[i][j] = next[i][k]

def path(u, v):
    path = []
    while u != v:
        if next[u][v] == None:
            return []
        path.append(u)
        u = next[u][v]
    return path

##### Bellman–Ford algorithm
# For finding shortest paths from a single source vertex to all other vertices in a directed weighted graph
# When having negative edge weight, it can detect negative cycles (i.e. a cycle whose edges sum to a negative value)
# O(VE)
dist = [INF] * V
dist[source] = 0
prev = [None] * V

for _ in range(V - 1):
# cuz longest possible path without a cycle can be V-1 edges
    for (u, v) in edges:
        if dist[u] + weight[u][v] < dist[v]:
            dist[v] = dist[u] + weight[u][v]
            prev[v] = u

# check for negative-weight cycles
for (u, v) in edges:
    if dist[u] + weight[u][v] < dist[v]:
        has_negative_cycle = True

##### Dijkstra's algorithm
# For finding shortest paths from a single source vertex to all other vertices in a directed weighted graph with non-negative weight only
# It uses min-priority queue for storing and querying partial solutions sorted by distance from the source
# Then greedily selects the minimum-weight node that has not yet been processed, and performs the relaxation process on all of its outgoing edges
# In contrast, the Bellman–Ford algorithm simply relaxes all the edges, and does V-1 times
# O((E+V)logV), or O(V^2) if using array
dist = [INF] * V
dist[source] = 0
not_checked_pq = [(dist[v], v) for v in range(V)]
prev = [None] * V

while not_checked_pq:
    current_v = not_checked_pq.get_min()
    not_checked_pq.remove(current_v)
    for v in not_checked_pq and edge[u][v] != None:
    # for neighbor v of u which are not yet checked
        if dist[u] + weight[u][v] < dist[v]:
            dist[v] = dist[u] + weight[u][v]
            prev[v] = u
            not_checked_pq.update((dist[v], v))

def path(target):
    path = []
    u = target
    while prev[u] != None:
        path.insert(0, u)
        u = prev[u]