# Irrefutable Outcome
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777c68
# dp with cache, O(N^2), pass test set 2

def opponent(player):
    return 'O' if player == 'I' else 'I'

def dp(board, current_player):
    # print(board, current_player)
    if (board, current_player) in cache:
        return cache[(board, current_player)]

    if not board:
        cache[('', 'I')] = ['O', 1]
        cache[('', 'O')] = ['I', 1]
        return ['O', 1] if current_player == 'I' else ['I', 1]
    elif len(board) == 1:
        cache[('I', 'I')] = ['I', 1]
        cache[('O', 'O')] = ['O', 1]
        cache[('O', 'I')] = ['O', 2]
        cache[('I', 'O')] = ['I', 2]
        if board == current_player:
            return ['I', 1] if current_player == 'I' else ['O', 1]
        else:
            return ['O', 2] if current_player == 'I' else ['I', 2]
    else:
        if board[0] != current_player and board[-1] != current_player:
            cache[(board, current_player)] = [opponent(current_player), len(board) + 1]
            return [opponent(current_player), len(board) + 1]

        result1 = None
        result2 = None
        if board[0] == current_player:
            result1 = dp(board[1:], opponent(current_player))
        if board[-1] == current_player:
            result2 = dp(board[:-1], opponent(current_player))
        if result1 is not None and result2 is not None:
            # print("current", current_player, "compare", result1, result2)
            if result1[0] == result2[0] and result1[0] == current_player:
                final_result = max(result1, result2, key=lambda x: x[1])
            elif result1[0] == result2[0] and result1[0] == opponent(current_player):
                final_result = min(result1, result2, key=lambda x: x[1])
            else:
                final_result = result1 if result1[0] == current_player else result2
            cache[(board, current_player)] = final_result
            return final_result
        elif result1 is None:
            cache[(board, current_player)] = result2
            return result2
        elif result2 is None:
            cache[(board, current_player)] = result1
            return result1

T = int(input())
for t in range(T):
    B = input()

    cache = {}
    [winner, point] = dp(B, 'I')
    print(f"Case #{t + 1}: {winner} {point}")
