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
  int n, s, r;
  cin >> n >> s >> r;
  int diff = s - r;
  int res[n];
  res[0] = diff;
  int i = n - 1;
  while (i > 0) {
    int die = min((1 + r - i), 6);
    res[i--] = die;
    r -= die;
  }
  for (int num : res) {
    cout << num << " ";
  }
  cout << endl;
}

int main() {
  int tc; 
  cin >> tc; // read no. of test cases

  // solving for every test case
  while(tc--) {
    solve();
  }
}
