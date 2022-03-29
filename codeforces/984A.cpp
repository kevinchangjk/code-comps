#include <iostream>
#include <cmath>
#include <bits/stdc++.h> 

using namespace std;

int main() {
    
    int n;
    cin >> n;
    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums, nums + n);

    if (n % 2 == 0) {
        cout << nums[(n/2)-1];
    }

    else {
        cout << nums[n/2];
    }


}