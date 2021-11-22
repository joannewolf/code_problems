# Prime Time
# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007543d8

import math

T = int(input())
for t in range(T):
    M = int(input())
    sum = 0
    sum_N = 0
    primes = []
    for i in range(M):
        [P, N] = [int(n) for n in input().split()]
        sum += P * N
        sum_N += N
        primes.append((P, N))
    # print(sum, sum_N, primes)

    result = 0
    # Since the max(P) = 499, the # of card in second group can be up to log2(400 * sum_N)
    max_card = math.ceil(math.log2(499 * sum_N))
    # The possible sum of first group is sum - 499 * max_card ~ sum - 2
    for candidate in range(max(sum - 499 * max_card, 2), sum - 1):
        # See if candidate can be factored with existing primes
        temp_candidate = candidate
        used_primes = []
        used_primes_num = 0
        for i in range(M):
            fully_used = True
            for j in range(primes[i][1]):
                if (temp_candidate % primes[i][0] == 0):
                    temp_candidate //= primes[i][0]
                else:
                    fully_used = False
                    break
            if (fully_used):
                used_primes_num += j + 1
                used_primes.append((primes[i][0], j + 1))
            elif (j > 0):
                used_primes_num += j
                used_primes.append((primes[i][0], j))
            if (used_primes_num > max_card):
                break
        # print(candidate, temp_candidate, used_primes)
        if (temp_candidate == 1):
            # Candidate can be factored, see if sum - used_primes == candidate
            temp_sum = sum
            for used_prime in used_primes:
                temp_sum -= used_prime[0] * used_prime[1]
            # print(used_primes, temp_sum)
            if (temp_sum == candidate and candidate > result):
                result = candidate

    print("Case #{}: {}".format(t + 1, result))
