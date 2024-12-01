# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    INT_MAX = 1500000
    num_set = set(A)

    for i in range(1, INT_MAX):
        if i not in num_set:
            return i
