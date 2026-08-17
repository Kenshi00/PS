#include <string>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string solution(int age) {
    string answer = "";
    map<char, string> m;
    m['0'] = "a";
    m['1'] = "b";
    m['2'] = "c";
    m['3'] = "d";
    m['4'] = "e";
    m['5'] = "f";
    m['6'] = "g";
    m['7'] = "h";
    m['8'] = "i";
    m['9'] = "j";
    string temp = to_string(age);
    for(auto c : temp)
    {
        answer += m[c];
    }
    return answer;
}