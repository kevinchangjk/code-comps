#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int scalc(int n, int k) {
    if (k == 1) {
        return 1;
    }
    elif (n == 1) {
        return 2;
    }
    elif (k == 2) {
        return n+1;
    }
    else {
        int s[k-1];
        s[0] = n+1;
        int ss[n-1];
        int j = n-1;
        int count = 0;
        for (int i = 0; i < n-1; i++) {
            ss[i] = j;
            count += j;
            j--;
        }
        s[1] = count;
        for (int i = 0; i < k-3; i++) {
            int sss[n-1];
            for (int l = 0; l < n-1; l++) {
                int count = 0;
                for (int j = n-1; j > 0; j--) {
                    count += s[j];
                }
            }
            
        }
        }
    }

}

int main() {
    int pmod = 1000000007;
    int t;
    cin >> t;

    for (int i = 0; i<t; i++) {
        int n, k;
        cin >> n >> k;
        cout << scalc(n, k) << endl;
    }

}