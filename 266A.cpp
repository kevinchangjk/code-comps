#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 
#include <string>

using namespace std;

int main() {

    string colours;
    int res = 0;
    int n;
    cin >> n;
    cin >> colours;
    for (int i = 1; i < n; i++) {
        if (colours[i] == colours[i-1]) {
            res++;
        }
    }
    cout << res;
}