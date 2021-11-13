# Friends
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff49/000000000043aee7
# Use Floyd–Warshall algorithm to find all pair of shortest paths between letters
# O(L^2*N + 26^3 + L^2*Q) = O(L^2*(N+Q))

INF = pow(10, 5)
T = int(input())
for t in range(T):
    [N, Q] = [int(n) for n in input().split()]
    names = input().split()

    dist = [[INF] * 26 for i in range(26)]
    for i in range(26):
        dist[i][i] = 0
    # Letters have edge only if they appear in same name
    for i in range(N):
        names[i] = list(set(names[i]))
        L = len(names[i])
        for j in range(L):
            for k in range(j + 1, L):
                dist[ord(names[i][j]) - ord('A')][ord(names[i][k]) - ord('A')] = 1
                dist[ord(names[i][k]) - ord('A')][ord(names[i][j]) - ord('A')] = 1
    for k in range(26):
        for i in range(26):
            for j in range(26):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    dist_people = {}

    ans = []
    for i in range(Q):
        [x, y] = [int(n) for n in input().split()]
        if (x - 1, y - 1) not in dist_people:
            temp = INF
            for letter1 in names[x - 1]:
                for letter2 in names[y - 1]:
                    temp = min(temp, dist[ord(letter1) - ord('A')][ord(letter2) - ord('A')])
            # temp: # of edge in letter's graph, means there are temp + 1 letters are used to connect, means there are temp + 2 people in chain
            dist_people[(x - 1, y - 1)] = temp + 2 if temp != INF else -1
            dist_people[(y - 1, x - 1)] = dist_people[(x - 1, y - 1)]
        ans.append(dist_people[(x - 1, y - 1)])

    print(f"Case #{t + 1}: {' '.join([str(n) for n in ans])}")
