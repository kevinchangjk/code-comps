/**
 * Template C++ file for Codeforces problems.
 * Written by @kevinchangjk
 */

// #include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
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
  string lamps;
  
  for (int i = 0; i < n; i++) {
    char lamp;
    cin >> lamp;
    lamps += lamp;
  }

  int swap = -1;
  for (int i = 0; i < n; i++) {
    char lamp = lamps[i];
    if (lamp == 'R') {
      if (lamps[i + 1] == 'L') {
        cout << 0 << endl;
        return;
      } else {
        continue;
      }
    }

    if (swap == -1 && lamps[i + 1] == 'R') {
      swap = i + 1;
    } else {
      continue;
    }
  }

  cout << swap << endl;
}

int main() {
  int tc; 
  cin >> tc; // read no. of test cases

  // solving for every test case
  while(tc--) {
    solve();
  }
}
