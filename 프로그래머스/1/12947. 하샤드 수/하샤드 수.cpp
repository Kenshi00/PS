#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool solution(int x) {
    bool answer = true;
    int s = 0;
    int temp = x;
    while(temp)
    {
        s += temp % 10;
        temp /= 10;
    }
    if(x % s != 0) answer = false;
    return answer;
}