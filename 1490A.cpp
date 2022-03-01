#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 
#include <algorithm>

using namespace std;

int main() {
    
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        int a[n];
        int counts[n] = {0};
        for (int j = 0; j < n; j++) {
            cin >> a[j];
            
            if (j > 0) {
                double aj = a[j];
                double aj1 = a[j-1];
                double divi;
                if (a[j] > a[j-1]) {
                    divi = aj / aj1;
                }
                else {
                    divi = aj1 / aj;
                }
                int count = 0;
                while (divi > 2) {
                    divi = divi / 2;
                    count++;
                }
                counts[j] = count;
            }
        }

        int sum = 0;
        for (int k = 0; k < n ; k++) {
            sum += counts[k];
        }
        
        cout << sum << endl;
    }
}