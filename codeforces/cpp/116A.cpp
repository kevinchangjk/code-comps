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
  int stops;
  cin >> stops;

  int max = 0;
  int people = 0;

  for (int i = 0; i < stops; i++) {
    int exit, enter;
    cin >> exit >> enter;
    people = people - exit + enter;

    if (people > max) {
      max = people;
    }
  }

  cout << max << endl;
}

int main() {
  int tc; 
  tc = 1;

  // solving for every test case
  while(tc--) {
    solve();
  }
}
