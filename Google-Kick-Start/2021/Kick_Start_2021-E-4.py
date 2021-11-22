# Increasing Sequence Card Game
# https://codingcompetitions.withgoogle.com/kickstart/round/000000000043585c/000000000085a709
# When the top card is x, in the rest N-1 cards we only need to take care of cards which > x, i.e. x+1 ~ N
# Also, we only care the number of cards, but not the value of cards, so expected value for x+1 ~ N = expected value for 1 ~ N-x = E_(N-x)
# => when top card is x, expected score = E_(N-x) + 1
# => E_N = sum{x=1~N} E_(N-x) / N + 1 = sum{i=0~N-1} E_i / N + 1 = S_(N-1) / N + 1
# E_(N+1) = S_N / (N+1) + 1 = (E_N + S_(N-1)) / (N+1) + 1 = (S_(N-1) / N + 1 + S_(N-1)) / (N+1) + 1
# = S_(N-1) / N + 1 / (N+1) + 1 = E_N + 1 / (N+1)
# Since error can be within 10^-6, we can estimate when N > 10^6
# When N > 10^6, E_N = E_(10^6) + integral{10^6+1 ~ N} 1/x dx = E_(10^6) + log(N) - log(10^6-1)

import math

T = int(input())

E = [0, 1]
for i in range(2, pow(10, 6) + 1):
    E.append(E[-1] + 1 / i)

for t in range(T):
    N = int(input())
    if N <= pow(10, 6):
        result = E[N]
    else:
        result = E[-1] + math.log(N) - math.log(pow(10, 6) - 1)
    
    print(f"Case #{t + 1}: {result}")
