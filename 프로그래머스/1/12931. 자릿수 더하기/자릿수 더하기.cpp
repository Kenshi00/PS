#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int solution(int N)
{
    int answer = 0;
    while(N)
    {
        answer += N % 10;
        N /= 10;
    }
    return answer;
}