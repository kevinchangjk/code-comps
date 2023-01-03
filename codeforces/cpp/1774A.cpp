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
  char bin;
  cin >> bin;
  int count;
  if (bin == '1') {
    count = 1;
  } else {
    count = 0;
  }

  string res = "";
  for (int i = 1; i < n; i++) {
    char nbin;
    cin >> nbin;
    if (nbin == '1') {
      if (count > 0) {
        count--;
        res += '-';
      } else {
        count++;
        res += '+';
      }
    } else {
      res += '+';
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
