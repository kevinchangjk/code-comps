/**
 * Template C++ file for Codeforces problems.
 * Written by @kevinchangjk
 */

// #include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <string>
#include <cctype>
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
  string word;
  cin >> word;

  int len = word.length();
  int up = 0;
  bool upper = false;

  for (int i = 0; i < len; i++) {
    char curr = word[i];
    if (isupper(curr)) {
      up++;
    }
  } 

  if (up > word.length() / 2) {
    upper = true;
  }

  for (int i = 0; i < len; i++) {
    if (upper && !isupper(word[i])) {
      word[i] -= 32;
    } else if (!upper && isupper(word[i])) {
      word[i] += 32;
    }
  }

  cout << word;
}

int main() {
  int tc = 1;

  // solving for every test case
  while(tc--) {
    solve();
  }
}
