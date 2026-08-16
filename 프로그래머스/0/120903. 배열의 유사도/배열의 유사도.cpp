#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(vector<string> s1, vector<string> s2) {
    int answer = 0;
    for(auto c1 : s1)
    {
        for(auto c2 : s2)
        {
            if(c1 == c2)
            {
                answer++;
                break;
            }
        }
    }
    return answer;
}