// Prime Time
// https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007543d8

#include <iostream>
#include <vector>
#include <utility>
#include <math.h>
#include <algorithm>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        // get input for each case
        int M;
        cin >> M;
        long long sum_N = 0;
        long long sum = 0;
        vector< pair<int, long long> > primes;
        for (int i = 0; i < M; i++) {
            int P;
            long long N;
            cin >> P;
            cin >> N;
            sum += P * N;
            sum_N += N;
            primes.push_back(make_pair(P, N));
        }

        long long result = 0;
        // Since the max(P) = 499, the # of card in second group can be up to log2(400 * sum_N)
        int max_card = ceil(log2(499 * sum_N));
        // The possible sum of first group is sum - 499 * max_card ~ sum - 2
        for (long long candidate = max(sum - 499 * max_card, (long long)2); candidate < sum - 1; candidate++) {
            // See if candidate can be factored with existing primes
            long long temp_candidate = candidate;
            vector< pair<int, long long> > used_primes;
            int used_primes_num = 0;
            for (int i = 0; i < M; i++) {
                bool fully_used = true;
                for (int j = 0; j < primes[i].second; j++) {
                    if (temp_candidate % primes[i].first == 0) {
                        temp_candidate /= primes[i].first;
                    }
                    else {
                        fully_used = false;
                        used_primes_num += j;
                        used_primes.push_back(make_pair(primes[i].first, j));
                        break;
                    }
                }
                if (fully_used) {
                    used_primes_num += primes[i].second;
                    used_primes.push_back(make_pair(primes[i].first, primes[i].second));
                }
                if (used_primes_num > max_card)
                    break;
            }

            if (temp_candidate == 1) {
                // Candidate can be factored, see if sum - used_primes == candidate
                long long temp_sum = sum;
                for (int i = 0; i < used_primes.size(); i++) {
                    temp_sum -= used_primes[i].first * used_primes[i].second;
                }
                if (temp_sum == candidate && candidate > result)
                    result = candidate;
            }
        }
        printf("Case #%d: %lld\n", t + 1, result);
    }
}
