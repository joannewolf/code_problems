# Centauri Prime
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008f4332/0000000000941ec5

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

T = int(input())
for t in range(T):
    kingdom = input()
    if kingdom[-1] in vowels:
        ans = "Alice"
    elif kingdom[-1] == 'y' or kingdom[-1] == 'Y':
        ans = "nobody"
    else:
        ans = "Bob"

    print(f"Case #{t + 1}: {kingdom} is ruled by {ans}.")
