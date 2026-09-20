#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int cal(int n)
{
    int ans = 0;
    for(int i = 1; i <= n; i++)
    {
        if(n % i == 0) ans++;
    }
    return ans;
}

int solution(int left, int right) {
    int answer = 0;
    for(int i = left; i <= right; i++)
    {
        if(cal(i) % 2 == 0) answer += i;
        else answer -= i;
    }
    return answer;
}