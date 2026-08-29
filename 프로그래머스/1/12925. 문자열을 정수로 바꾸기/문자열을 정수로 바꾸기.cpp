#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int solution(string s) {
    int answer = 0;
    if(s.find("-") != string::npos)
    {
        answer -= stoi(s.substr(1));   
    }
    else
    {
        answer += stoi(s);
    }
    return answer;
}