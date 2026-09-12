#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(string s) {
    string answer = "";
    if(size(s) % 2 == 0)
    {
        int lt = size(s) / 2 - 1;
        int rt = size(s) / 2;
        answer += s[lt];
        answer += s[rt];
    }
    else
    {
        answer += s[size(s) / 2];
    }
    return answer;
}