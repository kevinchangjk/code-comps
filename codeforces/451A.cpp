#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int dec;
    if (n < m) {
        dec = n;
    }

    else {
        dec = m;
    }

    if (dec % 2 == 0) {
        cout << "Malvika" << endl;
    }

    else {
        cout << "Akshat" << endl;
    }




}