# Irrefutable Outcome
# https://codingcompetitions.withgoogle.com/codejamio/round/00000000004360f2/0000000000777c68
# O(N)

def opponent(player):
    return 'O' if player == 'I' else 'I'

T = int(input())
for t in range(T):
    B = input()

    current_player = 'I'
    done = False
    while B:
        if B[0] != current_player and B[-1] != current_player:
            print(f"Case #{t + 1}: {opponent(current_player)} {len(B) + 1}")
            done = True
            break
        elif len(B) == 1 or B[0] != B[-1]:
            if B[0] == current_player:
                B = B[1:]
            else:
                B = B[:-1]
            current_player = opponent(current_player)
            continue
        else:
            # Either side is current user, find the leftmost and rightmost II or OO
            left_ptr = -1
            right_ptr = -1
            for i in range(0, len(B) - 1):
                if B[i] == B[i + 1]:
                    left_ptr = i
                    break
            for i in range(len(B) - 1, 0, -1):
                if B[i] == B[i - 1]:
                    right_ptr = i
                    break
            # print("left_ptr", left_ptr, "right_ptr", right_ptr)

            if left_ptr == -1:
                # No II or OO, all pieces will be taken eventually
                if len(B) % 2 == 1:
                    print(f"Case #{t + 1}: {current_player} 1")
                else:
                    print(f"Case #{t + 1}: {opponent(current_player)} 1")
            elif B[left_ptr] != B[right_ptr]:
                # One side is II, the other side is OO, current player can win by choosing the current player's side
                if B[left_ptr] == current_player:
                    print(f"Case #{t + 1}: {current_player} {len(B[left_ptr+1:]) + 1}")
                else:
                    print(f"Case #{t + 1}: {current_player} {len(B[:right_ptr]) + 1}")
            elif B[left_ptr] == current_player:
                # Both side is II / OO for current user Izabella / Olga, current player can win, choose the max point
                print(f"Case #{t + 1}: {current_player} {max(len(B[left_ptr+1:]) + 1, len(B[:right_ptr]) + 1)}")
            else:
                # Both side is OO / II for current user Izabella / Olga, current player will lose, min opponent's point by using all IO's on both sides
                print(f"Case #{t + 1}: {opponent(current_player)} {right_ptr - left_ptr}")
            done = True
            break

    if not done:
        # All pieces are taken, board is clear
        print(f"Case #{t + 1}: {opponent(current_player)} 1")
