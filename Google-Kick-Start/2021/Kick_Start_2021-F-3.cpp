// Star Trappers
// https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000888d45
// The minimum polygon must be triangle or quadrilateral (where target is on the intersection of diagonals)
// If target is in quadrilateral but not in intersection of diagonals, it definitely can reduce to some triangle which has smaller perimeter

#include <iostream>
#include <vector>
#include <utility>
#include <math.h>
#include <algorithm>
#include <set>

#define ll long long

using namespace std;

ll MAX_INT = pow(10, 7);

ll sign(pair<ll, ll> p1, pair<ll, ll> p2, pair<ll, ll> p3) {
    return (p1.first - p3.first) * (p2.second - p3.second) - (p2.first - p3.first) * (p1.second - p3.second);
}

double get_perimeter(vector< pair<ll, ll> > points) {
    double result = 0;
    int N = points.size();
    for (int i = 0; i < N - 1; i++) {
        result += sqrt(pow(points[i].first - points[i + 1].first, 2) + pow(points[i].second - points[i + 1].second, 2));
    }
    result += sqrt(pow(points[0].first - points[N - 1].first, 2) + pow(points[0].second - points[N - 1].second, 2));
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int N;
        cin >> N;
        vector< pair<ll, ll> > stars;
        for (int i = 0; i < N; i++) {
            ll x, y;
            cin >> x >> y;
            stars.push_back(make_pair(x, y));
        }
        ll target_x, target_y;
        cin >> target_x >> target_y;
        pair<ll, ll> target = make_pair(target_x, target_y);

        set< pair<int, int> > target_on_lines;

        double result = MAX_INT;
        for (int i = 0; i < N - 2; i++) {
            for (int j = i + 1; j < N - 1; j++) {
                for (int k = j + 1; k < N; k++) {
                    ll d1 = sign(target, stars[i], stars[j]);
                    ll d2 = sign(target, stars[j], stars[k]);
                    ll d3 = sign(target, stars[k], stars[i]);
                    if (d1 == 0)
                        target_on_lines.insert(make_pair(i, j));
                    if (d2 == 0)
                        target_on_lines.insert(make_pair(j, k));
                    if (d3 == 0)
                        target_on_lines.insert(make_pair(i, k));

                    if ((d1 < 0 && d2 < 0 && d3 < 0) || (d1 > 0 && d2 > 0 && d3 > 0)) {
                        // Target in triangle
                        vector< pair<ll, ll> > triangle;
                        triangle.push_back(stars[i]);
                        triangle.push_back(stars[j]);
                        triangle.push_back(stars[k]);
                        double perimeter = get_perimeter(triangle);
                        if (perimeter < result)
                            result = perimeter;
                    }
                }
            }
        }

        if (!target_on_lines.empty()) {
            for (set< pair<int, int> >::iterator it = target_on_lines.begin(); it != prev(target_on_lines.end()); it ++) {
                for (set< pair<int, int> >::iterator it2 = next(it); it2 != target_on_lines.end(); it2 ++) {
                    pair<ll, ll> p1 = stars[it -> first];
                    pair<ll, ll> p2 = stars[it2 -> first];
                    pair<ll, ll> p3 = stars[it -> second];
                    pair<ll, ll> p4 = stars[it2 -> second];
                    ll d1 = sign(target, p1, p2);
                    ll d2 = sign(target, p2, p3);
                    ll d3 = sign(target, p3, p4);
                    ll d4 = sign(target, p4, p1);
                    if ((d1 < 0 && d2 < 0 && d3 < 0 && d4 < 0) || (d1 > 0 && d2 > 0 && d3 > 0 && d4 > 0)) {
                        // Target in quadrilateral
                        vector< pair<ll, ll> > quadrilateral;
                        quadrilateral.push_back(p1);
                        quadrilateral.push_back(p2);
                        quadrilateral.push_back(p3);
                        quadrilateral.push_back(p4);
                        double perimeter = get_perimeter(quadrilateral);
                        if (perimeter < result)
                            result = perimeter;
                    }
                }
            }
        }

        if (result == MAX_INT)
            printf("Case #%d: IMPOSSIBLE\n", t + 1);
        else
            printf("Case #%d: %f\n", t + 1, result);
    }
}
