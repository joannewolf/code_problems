// Catch Them All
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000201d29/0000000000201c9b
// In DP method, it only needs dp[i - 1] to calculate dp[i], we can rewrite the state transition equation
// Let S(i) = SUM{dist[i][j]}, j != i
//   +----------+   +---------------------------------------------+   +------------+
//   | dp[K, 1] |   |    0   , 1/(N-1), ... , 1/(N-1), S(1)/(N-1) |   | dp[K-1, 1] |
//   | dp[K, 2] |   | 1/(N-1),    0   , ... , 1/(N-1), S(2)/(N-1) |   | dp[K-1, 2] |
//   |   ...    | = |   ...  ,   ...  , ... ,   ...  ,     ...    | * |    ...     |
//   | dp[K, N] |   | 1/(N-1), 1/(N-1), ... ,    0   , S(N)/(N-1) |   | dp[K-1, N] |
//   |    1     |   |    0   ,    0   , ... ,    0   ,     1      |   |     1      |
//   +----------+   +---------------------------------------------+   +------------+
// Let F_K be column vector of dp[K, i], and let A denote the transition matrix
// -> F_K = A * F_(K-1) = A^K * F_0
// O(N^3 + N^3*log(P))

#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll INF = pow(10, 5);

vector< vector<double> > matrix_multi(vector< vector<double> > A, vector< vector<double> > B) {
    assert(A[0].size() == B.size());
    vector< vector<double> > result(A.size(), vector<double>(B[0].size(), 0.0));
    for (int i = 0; i < A.size(); i++) {
        for (int k = 0; k < A[0].size(); k++) {
            for (int j = 0; j < B[0].size(); j++)
                result[i][j] += A[i][k] * B[k][j];
        }
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N, M, P;
        cin >> N >> M >> P;
        vector< vector<int> > dist(N, vector<int>(N, INF));
        for (int i = 0; i < N; i++)
            dist[i][i] = 0;
        for (int i = 0; i < M; i++) {
            int u, v, d;
            cin >> u >> v >> d;
            dist[u-1][v-1] = d;
            dist[v-1][u-1] = d;
        }
        
        // Use Floyd–Warshall algorithm to find all pairs of shortest paths
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
        
        vector< vector< vector<double> > > A; // A[i] = base_matrix ^ (2 ^ i)
        vector< vector<double> > base_matrix;
        for (int i = 0; i < N; i++) {
            double dist_sum = 0;
            for (int j = 0; j < N; j++) {
                if (j != i)
                    dist_sum += dist[i][j];
            }
            vector<double> row(N, (double)1 / (double)(N-1));
            row.push_back(dist_sum / (double)(N-1));
            row[i] = 0.0;
            base_matrix.push_back(row);
        }
        vector<double> row(N, 0.0);
        row.push_back(1.0);
        base_matrix.push_back(row);
        A.push_back(base_matrix);
        
        for (int i = 1; i <= ceil(log2(P)); i++) {
            A.push_back(matrix_multi(A.back(), A.back()));
        }

        vector< vector<double> > unit_matrix;
        for (int i = 0; i <= N; i++) {
            vector<double> row(N+1, 0.0);
            row[i] = 1.0;
            unit_matrix.push_back(row);
        }

        vector< vector<double> > A_P = unit_matrix;
        int bits = ceil(log2(P));
        for (int i = 0; i <= bits; i++) {
            if (P & 1) {
                A_P = matrix_multi(A_P, A[i]);
            }
            P /= 2;
        }

        printf("Case #%d: %f\n", t + 1, A_P[0][N]);
    }
}
