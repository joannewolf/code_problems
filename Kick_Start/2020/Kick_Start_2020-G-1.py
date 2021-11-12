# Kick_Start
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000001a0069/0000000000414bfb

T = int(input())
for t in range(T):
    S = input()
    N = len(S)

    kick_index = []
    start_index = []
    for i in range(N - 3):
        if S[i: i + 4] == "KICK":
            kick_index.append(i)
    for i in range(N - 4):
        if S[i: i + 5] == "START":
            start_index.append(i)
    
    ans = 0
    flag_k = 0
    flag_s = 0
    while flag_k < len(kick_index) and flag_s < len(start_index):
        if kick_index[flag_k] < start_index[flag_s]:
            ans += len(start_index) - flag_s
            flag_k += 1
        else:
            flag_s += 1

    print(f"Case #{t + 1}: {ans}")
