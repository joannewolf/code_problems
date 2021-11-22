# Painters' Duel
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff48/00000000003f47fb
# Brute-Force

def paint(empty_room, A_room, B_room, A_turn):
    # print(empty_room, "A", A_room, "B", B_room, A_turn)
    # Both A and B cannot move
    if A_room[-1] == (0, 0) and B_room[-1] == (0, 0):
        # print("return", len(A_room), len(B_room))
        return len(A_room) - len(B_room)
    # A cannot move
    if A_room[-1] == (0, 0) and A_turn:
        return paint(empty_room, A_room, B_room, not A_turn)
    # B cannot move
    if B_room[-1] == (0, 0) and not A_turn:
        return paint(empty_room, A_room, B_room, not A_turn)

    (s, p) = A_room[-1] if A_turn else B_room[-1]
    score = -50 if A_turn else 50
    cannot_move = True

    # Left room
    if p != 1 and (s, p - 1) in empty_room:
        cannot_move = False
        temp_empty_room = empty_room.copy()
        temp_empty_room.remove((s, p - 1))
        if A_turn:
            temp_score = paint(temp_empty_room, A_room + [(s, p - 1)], B_room, not A_turn)
            score = max(score, temp_score)
        else:
            temp_score = paint(temp_empty_room, A_room, B_room + [(s, p - 1)], not A_turn)
            score = min(score, temp_score)
    # Right room
    if p != 2 * s - 1 and (s, p + 1) in empty_room:
        cannot_move = False
        temp_empty_room = empty_room.copy()
        temp_empty_room.remove((s, p + 1))
        if A_turn:
            temp_score = paint(temp_empty_room, A_room + [(s, p + 1)], B_room, not A_turn)
            score = max(score, temp_score)
        else:
            temp_score = paint(temp_empty_room, A_room, B_room + [(s, p + 1)], not A_turn)
            score = min(score, temp_score)
    # Up room
    if p % 2 == 0 and (s - 1, p - 1) in empty_room:
        cannot_move = False
        temp_empty_room = empty_room.copy()
        temp_empty_room.remove((s - 1, p - 1))
        if A_turn:
            temp_score = paint(temp_empty_room, A_room + [(s - 1, p - 1)], B_room, not A_turn)
            score = max(score, temp_score)
        else:
            temp_score = paint(temp_empty_room, A_room, B_room + [(s - 1, p - 1)], not A_turn)
            score = min(score, temp_score)
    # Down room
    if p % 2 == 1 and (s + 1, p + 1) in empty_room:
        cannot_move = False
        temp_empty_room = empty_room.copy()
        temp_empty_room.remove((s + 1, p + 1))
        if A_turn:
            temp_score = paint(temp_empty_room, A_room + [(s + 1, p + 1)], B_room, not A_turn)
            score = max(score, temp_score)
        else:
            temp_score = paint(temp_empty_room, A_room, B_room + [(s + 1, p + 1)], not A_turn)
            score = min(score, temp_score)

    if cannot_move and A_turn:
        return paint(empty_room, A_room + [(0, 0)], B_room, not A_turn)
    elif cannot_move and not A_turn:
        return paint(empty_room, A_room, B_room + [(0, 0)], not A_turn)
    else:
        return score

T = int(input())
for t in range(T):
    [S, R_A, P_A, R_B, P_B, C] = [int(n) for n in input().split()]
    empty_room = set()
    A_room = []
    B_room = []
    for i in range(1, S + 1):
        for j in range(1, 2 * i):
            empty_room.add((i, j))
    A_room.append((R_A, P_A))
    empty_room.remove((R_A, P_A))
    B_room.append((R_B, P_B))
    empty_room.remove((R_B, P_B))
    for i in range(C):
        [r, p] = [int(n) for n in input().split()]
        empty_room.remove((r, p))

    print(f"Case #{t + 1}: {paint(empty_room, A_room, B_room, True)}")
