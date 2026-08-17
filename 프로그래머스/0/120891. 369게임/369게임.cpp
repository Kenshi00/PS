#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int order) {
    int answer = 0;
    while(order != 0)
    {
        int r = order % 10;
        if(r != 0 && r % 3 == 0) answer++;
        order /= 10;
    }
    return answer;
}