#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int w;
    string res;
    cin >> w;
    if (w % 2 == 0 && w > 2) {
        res = "YES";
    }
    else {
        res = "NO";
    }
    cout << res;
}