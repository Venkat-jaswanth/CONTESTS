#include <bits/stdc++.h>
using namespace std;

inline int getClassRep(int x, int k) {
    int r = x % k;
    return min(r, (k - r) % k);
}

bool solveOne() {
    int n, k;
    cin >> n >> k;
    unordered_map<int, int> scount, tcount;

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        ++scount[getClassRep(x, k)];
    }

    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        ++tcount[getClassRep(x, k)];
    }

    return scount == tcount;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        cout << (solveOne() ? "YES\n" : "NO\n");
    }
    return 0;
}
