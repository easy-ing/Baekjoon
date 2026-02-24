#include <bits/stdc++.h>
using namespace std;

// 안전한 unordered_map 해시 (해킹 방지)
struct SplitMix64 {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }
    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM =
            chrono::steady_clock::now().time_since_epoch().count();
        return (size_t)splitmix64(x + FIXED_RANDOM);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<unsigned long long> X(N);
    for (int i = 0; i < N; i++) cin >> X[i];

    // unique y 목록 만들기
    sort(X.begin(), X.end());
    vector<unsigned long long> Y;
    Y.reserve(N);
    for (int i = 0; i < N; ) {
        int j = i;
        while (j < N && X[j] == X[i]) j++;
        Y.push_back(X[i]);
        i = j;
    }
    int M = (int)Y.size();

    const int INF = 1e9;
    vector<int> best(M, INF);

    // t = 1..60에 대해 residue 카운트
    for (int t = 1; t <= 60; t++) {
        unsigned long long mask = (1ULL << t) - 1ULL;

        unordered_map<unsigned long long, int, SplitMix64> cnt;
        cnt.reserve((size_t)N * 2);
        cnt.max_load_factor(0.7f);

        for (auto x : X) {
            cnt[x & mask]++;
        }

        // 각 y에 대해 m <= c_t(y) + t - 1 갱신
        for (int i = 0; i < M; i++) {
            unsigned long long r = Y[i] & mask;
            int c = cnt[r];
            best[i] = min(best[i], c + t - 1);
        }
    }

    int ans = 1;
    for (int i = 0; i < M; i++) ans = max(ans, best[i]);
    cout << ans << "\n";
    return 0;
}