#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    // lcm
    int l = lcm(denom1, denom2);
    int temp1 = l / denom1, temp2 = l / denom2;
    numer1 *= temp1;
    numer2 *= temp2;
    int numer3 = numer1 + numer2;
    // gcd
    int g = gcd(numer3, l);
    answer.push_back(numer3 / g);
    answer.push_back(l / g);
    return answer;
}