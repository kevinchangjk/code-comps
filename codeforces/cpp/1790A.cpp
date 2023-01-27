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
  string pi = "3141592653589793238462643383279";
  string n;
  int res = 0;
  cin >> n;
  int len = n.length();
  for (int i = 0; i < len; i++) {
    if (n[i] == pi[i]) {
      res++;
    } else {
      cout << res << endl;
      return;
    }
  }
  cout << res << endl;
}

int main() {
  int tc; 
  cin >> tc; // read no. of test cases

  // solving for every test case
  while(tc--) {
    solve();
  }
}
