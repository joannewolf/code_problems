# Silly Substitutions
# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435914/00000000008d94f5
# Brute-force, O(N*10N) = O(N^2)

old_str = ['01', '12', '23', '34', '45', '56', '67', '78', '89', '90']
new_str = ['2', '3', '4', '5', '6', '7', '8', '9', '0', '1']

T = int(input())
for t in range(T):
    N = int(input())
    S = input()

    while True:
        no_more_change = True
        for i in range(10):
            new_S = S.replace(old_str[i], new_str[i])
            if new_S != S:
                no_more_change = False
                S = new_S
        if no_more_change:
            break

    print(f"Case #{t + 1}: {S}")
