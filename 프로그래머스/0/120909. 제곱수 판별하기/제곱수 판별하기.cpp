#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(int n) {
    int answer = 2;
    for(int i = 1; i <= 1000; i++)
    {
        if(pow(i,2) == n)
        {
            answer = 1;
        }
    }
    return answer;
}