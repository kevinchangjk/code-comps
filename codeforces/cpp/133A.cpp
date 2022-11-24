#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int main() {
    string p;
    cin >> p;
    int len = p.length();
    int i = 0;
    char var;
    bool resu = 0;
    while (resu != 1 & i != len) {
        var = p[i];
        if (var == 'H' || var == 'Q' || var == '9') {
            cout << "YES" << endl;
            resu = 1;
        }
        i++;
    }
    if (resu == 0) {
        cout << "NO" << endl;
    }


}