#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int solve() {
    int n, x, t;
    cin >> n >> x >> t;
    int dis = floor (t/x);
    int summa = (dis*(dis+1))/2;
    int total = (n * dis) - summa;
    cout << total << endl;
    return 0;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}