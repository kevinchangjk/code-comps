/**
 * Template C++ file for Codeforces problems.
 * Written by @kevinchangjk
 */

// #include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
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
  int a[n];
  for (int i = 0; i < n; i++) {
    cin >> a[i];
  }
  std::sort(a, a + n);

  vector<pii> groups;
  for (int i = 0; i < n; i++) {
    int aa = a[i];
    bool added = false;
    for (int j = 0; j < groups.size(); j++) {
      pii group = groups[j];
      if (aa == group.f - 1) {
        groups[j] = std::make_pair(aa, group.s);
        added = true;
        break;
      } else if (aa == group.s + 1) {
        groups[j] = std::make_pair(group.f, aa);
        added = true;
        break;
      } else {
        continue;
      }
    }

    if (!added) {
      groups.pb(std::make_pair(aa, aa));
    }
  }

  cout << groups.size() << endl;
}

int main() {
  int tc; 
  cin >> tc; // read no. of test cases

  // solving for every test case
  while(tc--) {
    solve();
  }
}
