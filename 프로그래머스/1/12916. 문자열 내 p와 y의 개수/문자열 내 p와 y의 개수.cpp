#include <string>
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    int temp_p = 0;
    int temp_y = 0;
    for(auto& c : s)
    {
        if(isupper(c)) c = tolower(c);
        if(c == 'p') temp_p++;
        else if(c == 'y') temp_y++;
    }
    if(temp_p != temp_y) answer = false;
    return answer;
}