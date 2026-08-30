#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

long long solution(long long n) {
    long long answer = 0;
    vector<int> v;
    while(n)
    {
        v.push_back(n % 10);
        n /= 10;
    }
    sort(v.rbegin(), v.rend());
    for(int i : v)
    {
        answer *= 10;
        answer += i;
    }
    return answer;
}