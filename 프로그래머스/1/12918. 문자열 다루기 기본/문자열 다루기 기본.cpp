#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if(!(size(s) == 4 || size(s) == 6)) answer = false;
    if(answer)
    {
        for(auto c : s)
        {
            if(!isdigit(c))
            {
                answer = false;
                break;
            }
        }
    }
    return answer;
}