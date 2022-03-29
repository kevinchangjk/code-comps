#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int main() {

    int n, q, suma = 0;
    cin >> n;
    cin >> q;
    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        if (a[i] == 1) {
            suma++;
        }
    }
    
    for (int i = 0; i < q; i++) {
        int qtype, xk, initv;
        cin >> qtype;
        cin >> xk;
        if (qtype == 1) {
            initv = a[--xk];
            a[xk] = 1-initv;
            suma = suma + 1 - initv - initv;
        }
        else {
            if (xk > suma) {
                cout << 0 << endl;
            }
            else {
                cout << 1 << endl;
            }
        }
        
    }


}