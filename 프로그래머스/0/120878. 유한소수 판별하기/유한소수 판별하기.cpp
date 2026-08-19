#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    int g = gcd(a,b);
    b /= g;
    while(1)
    {
        if(b % 2 == 0) b /= 2;
        else if(b % 5 == 0) b /= 5;
        else break;
    }
    if(b != 1) answer = 2;
    else answer = 1;
    return answer;
}