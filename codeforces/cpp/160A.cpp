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

    sort(a, a+n, greater<int>());
    int suma = 0;
    for (int i = 0; i < n; i++) {
        suma += a[i];
    }
    int summe = 0;
    int j = 0;
    
    while (summe <= suma) {
        summe += a[j];
        suma -= a[j];
        j++;
    }
    cout << j;

}