/**
 * Template C++ file for Codeforces problems.
 * Written by @kevinchangjk
 */

// #include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <string>
#define ll long long
#define f first
#define s second
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pb push_back
#define epb emplace_back
#define ull unsigned ll

using namespace std;

const int NMAX = 1e5 + 1;

// solution
void solve() {
  int n;
  cin >> n;
  if (n == 3) {
    cout << "NO" << endl;
  } else if (n % 2 == 0) {
    cout << "YES" << endl;
    int sig = 1;
    for (int i = 0; i < n; i++) {
      cout << sig << " ";
      sig *= -1;
    }
    cout << endl;
  } else {
    cout << "YES" << endl;
    int base = (n - 2) / 2;
    int inv = base * (-1) - 1;
    for (int i = 0; i < n; i++) {
      if (i % 2 == 0) {
        cout << base << " ";
      } else {
        cout << inv << " ";
      }
    }
    cout << endl;
  }
}

int main() {
  int tc; 
  cin >> tc; // read no. of test cases

  // solving for every test case
  while(tc--) {
    solve();
  }
}
