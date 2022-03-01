#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

void solve() {
    int s[4];
    int *ss = &s[0];
    int winners[2];
    for (int i = 0; i < 4; i++) {
        cin >> s[i];
    }
    winners[0] = max(s[0], s[1]);
    winners[1] = max(s[2], s[3]);
    sort(ss, ss+4);
    for (int i=0;i<2;i++) {
        if (winners[i] == s[0] || winners[i] == s[1]) {
            cout << "NO" << endl;
            return;
        }
    }
    cout << "YES" << endl;
}

int main() {
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }

}