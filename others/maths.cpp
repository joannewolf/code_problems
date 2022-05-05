constexpr int MOD = 1'000'000'007;
struct M {
    int v{};
    constexpr M(int x = 0) {
        if (x < -MOD || x >= MOD) x %= MOD;
        v = (x >= 0) ? x : x + MOD;
    }
    explicit constexpr operator int() const { return v; }
    constexpr bool operator==(const M& b) const { return v == b.v; }
    constexpr bool operator!=(const M& b) const { return v != b.v; }
    constexpr M operator-() const { return M(-v); }
    constexpr M operator+=(const M& b) { if ((v += b.v) >= MOD) v -= MOD; return *this; }
    constexpr M operator-=(const M& b) { if ((v -= b.v) < 0) v += MOD; return *this; }
    constexpr M operator*=(const M& b) { v = (long long)v * b.v % MOD; return *this; }
    constexpr M operator/=(const M& b) { return *this *= b ^ (MOD - 2); }
    constexpr friend M operator^(M a, int b) {
        M ret = 1;
        for (; b; a *= a, b >>= 1) if (b & 1) ret *= a;
        return ret;
    }
    constexpr friend M operator+(M a, const M& b) { return a += b; }
    constexpr friend M operator-(M a, const M& b) { return a -= b; }
    constexpr friend M operator*(M a, const M& b) { return a *= b; }
    constexpr friend M operator/(M a, const M& b) { return a /= b; }
    friend istream& operator>>(istream& i, M& m) {
        int x; i >> x, m = M(x); return i; }
    friend ostream& operator<<(ostream& o, M m) { return o << m.v; }
};
using Mod = M;
