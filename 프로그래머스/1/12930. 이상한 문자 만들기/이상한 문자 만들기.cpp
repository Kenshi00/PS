#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string s) {
    int cnt = 0;
    for(auto& c : s)
    {
        if(c == ' ') cnt = 0;
        else
        {
            if(cnt & 1) c = tolower(c);
            else c = toupper(c);
            cnt++;
        }
    }
    return s;
}