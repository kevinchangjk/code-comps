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
  string n;
  cin >> n;
  int lucky = 0;

  for (int i = 0; i < n.length(); i++) {
    char digit = n[i];
    if (digit == '4' || digit == '7') {
      lucky++;
    }
  }

  if (lucky == 4 || lucky == 7) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}

int main() {
  int tc; 
  tc = 1;

  // solving for every test case
  while(tc--) {
    solve();
  }
}
