# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # Implement your solution here
    N = len(A)
    for n in range(N): # shift n times
        all_pass = True
        for i in range(N):
            if A[i] == B[(i - n + N) % N]:
                all_pass = False
                break

        if all_pass:
            return n

    return -1
