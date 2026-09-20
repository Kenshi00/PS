#include <bits/stdc++.h>
using namespace std;

long long solution(int price, int money, int count)
{
    long long answer = -1;
    long long total_price = 0;
    for(long long i = 1; i <= count; i++)
    {
        total_price += i * price;
    }
    if(total_price - money > 0) answer = total_price - money;
    else answer = 0;
    return answer;
}