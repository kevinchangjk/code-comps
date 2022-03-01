#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    int n = (s.length() + 1) / 2;
    int summ[n];
    for (int i = 0; i < 2*n-1; i += 2) {
        string ss = s[i];
        summ[i/2] = stoi(ss);
    }
    int * pts;
    pts = &summ[0];
    sort(pts, pts+n);
    cout << summ[0];
    for (int i = 1; i < n; i++) {
        cout << "+" << summ[i];
    }
}