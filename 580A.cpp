#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    int streak[n] = {1};
    int stree = 1;
    int maxi = 1;

    for (int i = 1; i < n; i++) {
        if (a[i] >= a[i-1]) {
            stree++;
        }
        else {
            stree = 1;
        }
        streak[i] = stree;
        if (stree > maxi) {
            maxi = stree;
        }
    }

    cout << maxi << endl;


}