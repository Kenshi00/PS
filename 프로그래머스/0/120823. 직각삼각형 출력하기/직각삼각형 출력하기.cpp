#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

int main(void) {
    int n;
    cin >> n;
    for(int i = 1; i <= n; i++)
    {
        string star(i, '*');
        cout << star << endl;
    }
    return 0;
}