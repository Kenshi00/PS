#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

long long solution(long long n) {
    long long answer = -1;
    for(long long i = 1; i <= n; i++)
    {
        if(i * i == n) answer = pow(i+1 , 2);
        if(pow(i , 2) > n) break; // 시간 초과 막는 장치
    }
    return answer;
}